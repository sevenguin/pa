#-*- coding:utf-8 -*-
    
class UserRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'pa_user':
            return 'pa_user'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'pa_user':
            return 'pa_user'
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'pa_user' or \
            obj2._meta.app_label == 'pa_user': 
            return True
        return None
    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'pa_user':
            return db == 'pa_user'
        return None