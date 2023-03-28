#include "jobList.h"
#include <QProcess>
#include <QString>
#include <QDebug>

JobList::JobList(QObject *parent)
    : QObject(parent), jobScripts(nullptr) {}

QVector<JobItem> JobList::items() const { return mItems; }

bool JobList::setItemAt(int index, const JobItem &item) {
  if (index < 0 || index >= mItems.size())
    return false;
  const JobItem &oldItem = mItems.at(index);
  if (oldItem.name == item.name && oldItem.isActive == item.isActive)
    return false;
  mItems[index] = item;
  return true;
}

void JobList::setScriptHandler(ScriptHandler *handler) {
  jobScripts = handler;
  if (jobScripts) {
    connect(jobScripts, &ScriptHandler::processHasChanged, this,
            [=](QProcess::ProcessState state, QString jobName) {
              JobItem item;
              item.name = jobName;
              if (state == QProcess::Starting) {

                qDebug() << "is started";
                item.isActive = true;
              }
              if (state == QProcess::Running) {

                qDebug() << "is running";
                item.isActive = true;
              }
              if (state == QProcess::NotRunning) {

                qDebug() << "is stopped";
                item.isActive = false;
              }
              for (int i = 0; i < mItems.size(); i++) {
                if (mItems.at(i).name == jobName)
                  if (setItemAt(i, item))
                    emit indexChanged(i);
              }
            });
  }
}

void JobList::appendItem(JobItem item) {
  emit preItemAppended();
  mItems.append(item);
  emit postItemAppended();
}

void JobList::removeSingleItem(int index) {
  emit preItemRemoved(index);
  mItems.removeAt(index);
  emit postItemRemoved();
}

void JobList::removeCompletedItems() {
  for (int i = 0; i < mItems.size(); i++) {
    removeSingleItem(i);
  }
}

void JobList::changeState(QString name) {
  for (int i = 0; i < mItems.size(); i++) {
    if (mItems.at(i).name == name) {
      if (!mItems.at(i).isActive) {

        qDebug() << "start script";
        jobScripts->startScript(name);
      } else {

        qDebug() << "stopt script";
        jobScripts->stopScript();
      }
    }
  }
}
