#include "jobmodel.h"
#include "jobList.h"
#include <QDebug>

JobModel::JobModel(QObject *parent)
    : QAbstractListModel(parent), mList(nullptr) {}

int JobModel::rowCount(const QModelIndex &parent) const {
  if (parent.isValid() || !mList)
    return 0;
  return mList->items().size();
}

QVariant JobModel::data(const QModelIndex &index, int role) const {
  if (!index.isValid() || !mList)
    return QVariant();

  const JobItem item = mList->items().at(index.row());
  switch (role) {
  case JobName:
    return QVariant(item.name);
  case JobIsActiveRole:
    return QVariant(item.isActive);
  }
  return QVariant();
}

bool JobModel::setData(const QModelIndex &index, const QVariant &value,
                       int role) {
  if (!mList)
    return false;
  JobItem item = mList->items().at(index.row());
  switch (role) {
  case JobName:
    item.name = value.toString();
    break;
  case JobIsActiveRole:
    item.isActive = value.toBool();
    break;
  }

  if (mList->setItemAt(index.row(), item)) {
    emit dataChanged(index, index, QVector<int>() << role);
    return true;
  }
  return false;
}

Qt::ItemFlags JobModel::flags(const QModelIndex &index) const {
  if (!index.isValid())
    return Qt::NoItemFlags;

  return Qt::ItemIsEditable;
}

QHash<int, QByteArray> JobModel::roleNames() const {
  QHash<int, QByteArray> names;
  names[JobName] = "name";
  names[JobIsActiveRole] = "isActive";
  return names;
}

JobList *JobModel::list() const { return mList; }

void JobModel::setList(JobList *list) {
  beginResetModel();
  if (mList)
    mList->disconnect(this);

  mList = list;

  if (mList) {
    connect(mList, &JobList::preItemAppended, this, [=]() {
      const int index = mList->items().size();
      beginInsertRows(QModelIndex(), index, index);
    });
    connect(mList, &JobList::postItemAppended, this,
            [=]() { endInsertRows(); });

    connect(mList, &JobList::preItemRemoved, this,
            [=](int index) { beginRemoveRows(QModelIndex(), index, index); });

    connect(mList, &JobList::postItemRemoved, this, [=]() { endRemoveRows(); });

    connect(mList, &JobList::indexChanged, this, [=](int pos) {
      // FROM https://stackoverflow.com/a/63177787
      dataChanged(index(pos), index(pos));
    });
  }

  endResetModel();
}
