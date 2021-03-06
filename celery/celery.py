from celery import Celery

app = Celery('proj',
             include=['celery.tasks'])

app.config_from_object('celeryconfig')
app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()
