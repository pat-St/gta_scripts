#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QQuickView>

#include "jobList.h"
#include "jobmodel.h"
#include "scriptHandler.h"
#include "processoutputlog.h"
#include <QDir>
#include <QFileInfo>
#include <QProcess>
#include <stdio.h>
#include <QDebug>


int main(int argc, char *argv[]) {
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
  QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif
  QGuiApplication app(argc, argv);

  qmlRegisterType<JobModel>("Job", 1, 0, "JobModel");
  qmlRegisterUncreatableType<JobList>(
      "Job", 1, 0, "JobList",
      QStringLiteral("JobList should not be created in QML"));
  qmlRegisterType<ProcessOutputLog>("Job", 1, 0, "ProcessOutputLog");

  ScriptHandler s_handler;
  QDir startPath(QDir::current());
  startPath.cdUp();
  qDebug() << startPath.cd("jobs");
  s_handler.setPath(startPath.absolutePath());
  JobList jobList;
  jobList.setScriptHandler(&s_handler);
  for (QString &jobName : s_handler.getScripts()) {
    jobList.appendItem({jobName, false});
  }

  QQmlApplicationEngine engine;
  const QUrl url(QStringLiteral("qrc:/main.qml"));

  QObject::connect(
      &engine, &QQmlApplicationEngine::objectCreated, &app,
      [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
          QCoreApplication::exit(-1);
      },
      Qt::QueuedConnection);
  engine.rootContext()->setContextProperty(QStringLiteral("jobList"), &jobList);
  engine.rootContext()->setContextProperty(QStringLiteral("scriptHandler"), &s_handler);
  engine.load(url);
  return app.exec();
}
