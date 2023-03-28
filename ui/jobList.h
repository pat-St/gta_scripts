#ifndef JOBLIST_H
#define JOBLIST_H
#include <QVector>
#include <QObject>
#include "scriptHandler.h"

struct JobItem {
    QString name;
    bool isActive;
};

class JobList : public QObject
{
    Q_OBJECT
public:
    explicit JobList(QObject *parent = nullptr);

    QVector<JobItem> items() const;
    JobList* list() const;

    void setList(JobList *list);
    bool setItemAt(int index, const JobItem &item);

    void setScriptHandler(ScriptHandler *handler);

signals:
    void preItemAppended();
    void postItemAppended();

    void preItemRemoved(int index);
    void postItemRemoved();

    void indexChanged(int index);

public slots:
    void appendItem(JobItem item);
    void removeSingleItem(int index);
    void removeCompletedItems();
    void changeState(QString name);

private:
    QVector<JobItem> mItems;
    ScriptHandler *jobScripts;
};

#endif // JOBLIST_H
