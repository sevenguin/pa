# -*- coding: utf-8 -*-
"""
    问题配置文件
"""

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
            'proc_func': 'introduce',  #处理回答该问题的方法  
            'proc_model': 'pa_manager',     #处理回答该问题的模块
            'answer_type': 'text',
            'answer_value': 'None'    #只有当answer_type是choice的时候，这个才是选择的列表例如是、否            
        }
    },
    'manager':{

    },
    'servant':{
        '0':{ #key is questionid
            'questioninfo':'None',
            'answer_table':'None',
            'answer_field':'None',
            'topicid': '0', #0表示用户主动发送信息
            'proc_func': 'pa_message',
            'proc_model': 'activerequestion'
        }
    }
}

models = {
    'greeting':{
        '0': {
            'next_question': '1', 
            'next_question_model':'greeting'
        }     #cur_question：{next_question}
    }
}