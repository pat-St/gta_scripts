#ifndef PROCESSOUTPUTLOG_H
#define PROCESSOUTPUTLOG_H
#include <QAbstractListModel>

#include <QStringList>
#include <QStringListModel>

#include "scriptHandler.h"

struct ProcessLogItem {
    QString output;
};

class ProcessOutputLog : public QAbstractListModel
{
    Q_OBJECT
    Q_PROPERTY(QList<ProcessLogItem> list READ list WRITE setList)
    Q_PROPERTY(ScriptHandler* sh READ sh WRITE setSh)

public:
    ProcessOutputLog(QObject *parent = nullptr);

    enum {
        Output = Qt::UserRole
    };

    int rowCount(const QModelIndex &parent = QModelIndex()) const override;

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;

    // Editable:
    bool setData(const QModelIndex &index, const QVariant &value,
                 int role = Qt::EditRole) override;

    Qt::ItemFlags flags(const QModelIndex& index) const override;

    virtual QHash<int,QByteArray> roleNames() const override;

    QList<ProcessLogItem> list() const;

    void setList(const QList<ProcessLogItem> &list);

    void setSH(ScriptHandler *list);


    ScriptHandler *sh() const;
    void setSh(ScriptHandler *newSh);

private:
    ScriptHandler *m_sH;
    QList<ProcessLogItem> mItems;

private slots:

signals:
};

#endif // PROCESSOUTPUTLOG_H
