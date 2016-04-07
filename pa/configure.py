# -*- coding:utf-8 -*-

provinces = {
	'陕西':{
		'mainfood': 'noodle',
		'snack': ['凉皮', '面条', '肉夹馍', '羊肉泡馍'],   #小吃
		'location': 'west north',
		'neighbors': ['四川', '甘肃', '宁夏', '内蒙古', '山西', '河南', '河北', '湖北', '重庆']
	},
	'黑龙江':{
		'mainfood': 'noodle',
		'snack': [],
		'location': 'east north'
	}
}

foodlabels = {
	'China':{'菜系':['鲁菜', '川菜', '粤菜', '苏菜', '闽菜', '浙菜', '湘菜', '徽菜'],
			 '味道':['偏甜', '超甜', '偏辣', '超辣']},
	'Foreign':{
		'State':['西餐', '日菜', '韩菜']
	}
}