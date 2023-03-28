#include "processoutputlog.h"
#include "scriptHandler.h"
#include <QDebug>
#include <QProcess>
#include <QStringList>
#include <iostream>
#include <QDate>

ProcessOutputLog::ProcessOutputLog(QObject *parent)
    : QAbstractListModel(parent), m_sH(nullptr), mItems() {
}

int ProcessOutputLog::rowCount(const QModelIndex &parent) const {
    if (parent.isValid() || mItems.empty())
        return 0;
    return (int)mItems.size();
}

QVariant ProcessOutputLog::data(const QModelIndex &index, int role) const {
    if (!index.isValid() || mItems.empty())
        return QVariant();

    ProcessLogItem item = mItems.at(index.row());
    switch (role) {
    case Output:
        return QVariant(item.output);
    }
    return QVariant();
}

bool ProcessOutputLog::setData(const QModelIndex &index, const QVariant &value,
                               int role) {
    if (mItems.empty())
        return false;
    ProcessLogItem item = mItems.at(index.row());
    switch (role) {
    case Output:
        item.output = value.toString();
        break;
    default:
        return false;
    }
    mItems.insert(index.row(), item);
    emit dataChanged(index, index, QVector<int>() << role);
    return true;
}

Qt::ItemFlags ProcessOutputLog::flags(const QModelIndex &index) const {
    if (!index.isValid())
        return Qt::NoItemFlags;

    return Qt::ItemIsEnabled;
}

QHash<int, QByteArray> ProcessOutputLog::roleNames() const {
    QHash<int, QByteArray> names;
    names[Output] = "output";
    return names;
}

QList<ProcessLogItem> ProcessOutputLog::list() const { return mItems; }

void ProcessOutputLog::setList(const QList<ProcessLogItem> &list) {
    mItems = list;
}

ScriptHandler *ProcessOutputLog::sh() const { return m_sH; }
void ProcessOutputLog::setSh(ScriptHandler *newSh) {
    beginResetModel();
//    if (newSh)
//        m_sH->disconnect(this);

    m_sH = newSh;

    if (m_sH) {
        connect(m_sH, &ScriptHandler::processHasChanged, this,
                [=](QProcess::ProcessState state, QString jobName) {
            Q_UNUSED(jobName);
            if (state == QProcess::Starting) {
                const int index = mItems.size();
                beginInsertRows(QModelIndex(), index, index);
                QString text(jobName);
                text += "\t";
                text += QDate::currentDate().toString(Qt::ISODateWithMs);
                mItems.append(ProcessLogItem{text});
                endInsertRows();
                //                beginRemoveRows(QModelIndex(), 0,
                //                mItems.size() - 1); mItems.clear();
                //                endRemoveRows();
                ;
            }
        });

        connect(m_sH, &ScriptHandler::processContent, this,
                [=](QString processText) {
            if (processText.isEmpty())
                return;
            const int index = mItems.size();
            beginInsertRows(QModelIndex(), index, index);
            mItems.append(ProcessLogItem{processText});
            endInsertRows();
        });
    }

    endResetModel();
}
