#ifndef JOBMODEL_H
#define JOBMODEL_H

#include <QAbstractListModel>

Q_MOC_INCLUDE("jobList.h")

class JobList;

class JobModel : public QAbstractListModel
{
    Q_OBJECT
    Q_PROPERTY(JobList *list READ list WRITE setList)

public:
    explicit JobModel(QObject *parent = nullptr);

    enum {
        JobName = Qt::UserRole + 1,
        JobIsActiveRole = Qt::UserRole + 2,
    };

    // Basic functionality:
    int rowCount(const QModelIndex &parent = QModelIndex()) const override;

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;

    // Editable:
    bool setData(const QModelIndex &index, const QVariant &value,
                 int role = Qt::EditRole) override;

    Qt::ItemFlags flags(const QModelIndex& index) const override;

    virtual QHash<int,QByteArray> roleNames() const override;

    JobList *list() const;

    void setList(JobList *list);

private:
    JobList *mList;

private slots:

signals:
};

#endif // JOBMODEL_H
