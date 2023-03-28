#include "scriptHandler.h"
#include <QDebug>
#include <QDir>
#include <QFileInfo>
#include <QFuture>
#include <QProcess>

// FROM https://stackoverflow.com/a/65184134
// #pragma push_macro("slots")
// #undef slots
// #include <Python.h>
// #pragma pop_macro("slots")

ScriptHandler::ScriptHandler(QObject *parent)
    : QObject(parent), jobFiles(0), runningProcess(nullptr) {
}

bool ScriptHandler::setPath(QString path) {
  scriptPath = path;
  return findJobs();
}

bool ScriptHandler::findJobs() {
  QDir dirs(scriptPath);
  if (!dirs.exists())
    return false;
  dirs.setFilter(QDir::Files | QDir::Readable);
  dirs.setSorting(QDir::Name);
  QFileInfoList pythonFiles = dirs.entryInfoList();
  QVector<QFileInfo> v(0);
  for (QFileInfo &pyFile : pythonFiles) {
    if (pyFile.baseName().endsWith("job"))
      v.append(pyFile);
  }
  jobFiles = std::move(v);
  return true;
}

QFileInfo ScriptHandler::getJobInfo(QString &jobName) {
  QFileInfo foundJob;
  for (auto &job : jobFiles) {
    if (job.baseName().replace("_job", "") == jobName) {
      foundJob = job;
    }
  }
  return foundJob;
}

QVector<QString> ScriptHandler::getScripts() {
  QVector<QString> scripts(0);
  for (QFileInfo &job : jobFiles) {
    QString jobName = job.baseName().replace("_job", "");
    scripts.append(jobName);
  }
  return scripts;
}

bool ScriptHandler::execProcess(QDir &projectRootDir, QString &scriptBaseName) {
  if (runningProcess != nullptr &&
      runningProcess->state() == QProcess::Running) {
    return false;
  }
  runningProcess = new QProcess();
  //      runningProcess->setProcessChannelMode(QProcess::ForwardedOutputChannel);
  runningProcess->setWorkingDirectory(projectRootDir.absolutePath());
  eventHandling();
  QString command = "python3";
  QStringList arguments;
  if (projectRootDir.exists(".venv")) {
    //        arguments << "-m"
    //                  << ".venv";
    command = ".venv/bin/python3";
  }
  arguments << scriptBaseName;
  runningProcess->start(command, arguments);
  QList<QString> processJobArgs = runningProcess->arguments();
  foreach (const QString &a, processJobArgs) {
    qDebug() << a;
  }

  return true;
}

bool ScriptHandler::stopScript() {
  // running process started before?
  // Is is running yet
  if (runningProcess->state() == QProcess::Running) {
    runningProcess->terminate();
  }
  // Wait for fishish
  if (!runningProcess->waitForFinished(100)) {
    runningProcess->terminate();
  }
  if (runningProcess->exitCode() > 0) {

    qDebug() << runningProcess->errorString();
  } else {

    qDebug() << runningProcess->processId();
  }
  delete runningProcess;
  runningProcess = nullptr;
  return true;
}

bool ScriptHandler::startScript(QString &jobName) {
  QFileInfo foundJob = getJobInfo(jobName);
  QDir parentdir(foundJob.dir());
  if (!(parentdir.isAbsolute() && parentdir.cdUp())) {
    return false;
  }
  QString jobScriptBaseName = foundJob.absoluteFilePath();
  return execProcess(parentdir, jobScriptBaseName);
}

void ScriptHandler::eventHandling() {
  //  if (runningProcess)
  //    runningProcess->disconnect(this);
  if (runningProcess) {
    connect(runningProcess, &QProcess::readyReadStandardOutput, this, [=]() {
      QByteArray result = runningProcess->readAll();
      emit processContent(QString(result.data()));
    });

    connect(runningProcess, &QProcess::stateChanged, this,
            [=](QProcess::ProcessState state) {
              QList<QString> processJobArgs = runningProcess->arguments();
              QFileInfo processFile(processJobArgs.last());
              QString jobName = processFile.baseName().replace("_job", "");
              emit processHasChanged(state, jobName);
            });
  }
}
