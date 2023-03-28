#ifndef SCRIPTHANDLER_H
#define SCRIPTHANDLER_H
#include <QDir>
#include <QFileInfo>
#include <QObject>
#include <QProcess>

class ScriptHandler:
        public QObject {
    Q_OBJECT
public:
    explicit ScriptHandler(QObject *parent = nullptr);
    bool setPath(QString path);
    QVector<QString> getScripts();
    bool startScript(QString &jobName);
    bool stopScript();
signals:
    void processHasChanged(QProcess::ProcessState state,QString jobName);
    void processContent(QString processText);
private:
    QString scriptPath;
    QVector<QFileInfo> jobFiles;
    QProcess* runningProcess;
    bool findJobs();
    QFileInfo getJobInfo(QString &jobName);
    bool execProcess(QDir &workingDir, QString &scriptBaseName);
    void eventHandling();
};

#endif // SCRIPTHANDLER_H
