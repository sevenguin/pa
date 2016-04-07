# -*- coding: utf-8 -*-
"""
    问题配置文件
"""
#问题需要有一些补充数据的文件，例如：各个地方的小吃？
#还有自己喜欢的吃食等
questions = {
    'greeting':{
        '0':{
            'questioninfo':'Hi, 终于等到了你，my lord',
            'answer_table':'None',
            'answer_field':'None',
            'topicid': '1', #1表示机器主动发送
            'proc_func': 'welcome',  #处理回答该问题的方法  
            'proc_model': 'pa_greeting',     #处理回答该问题的模块
            'answer_type': 'text',
            'answer_value': 'None'    #只有当answer_type是choice的时候，这个才是选择的列表例如是、否
        },
        '1':{
            'questioninfo':'您还没有介绍自己呢，是否现在介绍一下？',
            'answer_table':'None',
            'answer_field':'None',
            'topicid': '1', #1表示机器主动发送
            'proc_func': 'welcome',  #处理回答该问题的方法  
            'proc_model': 'pa_greeting',     #处理回答该问题的模块
            'answer_type': 'choice',  
            'answer_value': 'None'    #只有当answer_type是choice的时候，这个才是选择的列表例如是、否            
        },
        '2':{
            'questioninfo':'好吧，稍后您在介绍自己吧',
            'answer_table':'None',
            'answer_field':'None',
            'topicid': '1', #1表示机器主动发送
            'proc_func': 'introduce',  #处理回答该问题的方法  
            'proc_model': 'pa_manager',     #处理回答该问题的模块
            'answer_type': 'text',  
            'answer_value': 'None'    #只有当answer_type是choice的时候，这个才是选择的列表例如是、否   
        }
    },
    'manager':{
        '1':{
            'questioninfo': '给自己起个名字吧？',
            'answer_table': 'users',
            'answer_field': 'name',
            'topicid': '1',
            'proc_func': 'setvalue',
            'proc_model': 'pa_manager',
            'answer_type': 'text',
            'answer_value': 'None'
        },
        '2':{
            'questioninfo': '你小时候都是在哪个地方生活的？',
            'answer_table': 'users',
            'answer_field': 'child_living_place',
            'topicid': '1',
            'proc_func': 'setvalue',
            'proc_model': 'pa_manager',
            'answer_type': 'choice',
            'answer_value': '是 否'
        },
        '3':{
            'questioninfo': '您曾经在哪些地方待过呢？',
            'answer_table': 'users',
            'answer_field': 'ever_living_place',
            'topicid': '1',
            'proc_func': 'setvalue',
            'proc_model': 'pa_manager',
            'answer_type': 'choice',
            'answer_value': 'None'
        },
        '4':{
            'questioninfo': '您对吃的东西有什么偏好吗？',
            'answer_table': 'users',
            'answer_field': 'food_favor',
            'topicid': '1',
            'proc_func': 'setvalue',
            'proc_model': 'pa_manager',
            'answer_type': 'choice',
            'answer_value': 'None'
        },
        '5':{
            'questioninfo': '您有特别喜欢吃的菜么？',
            'answer_table': 'users',
            'answer_field': 'food_prefer',
            'topicid': '1',
            'proc_func': 'setvalue',
            'proc_model': 'pa_manager',
            'answer_type': 'choice',
            'answer_value': 'None'
        }
    },
    'servant':{
        '1':{ #key is questionid
            'questioninfo':'None',
            'answer_table':'None',
            'answer_field':'None',
            'topicid': '0', #0表示用户主动发送信息
            'proc_func': 'activerequestion',
            'proc_model': 'pa_message'
        }
    }
}

models = {
    'greeting':{
        '0': { #这个是questionid
            #这个是状态，0是默认，只有这一个值
            'next_question_model':'greeting',
            'next_question': '1'
        },     #cur_question：{next_question}
        '1': {
            #不同status不同的跳转，只有choice才有状态
            '1':{
                'next_question_model': 'manager',
                'next_question': '1'
            },
            '2':{
                'next_question_model': 'greeting',
                'next_question': '2'
            }
        }
    },
    'manager':{
        '1':{
            'next_question_model': 'manager',
            'next_question': '2'
        }
    }
}

