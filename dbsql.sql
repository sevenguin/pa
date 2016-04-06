CREATE TABLE `pa_message_t_questions` (
  `questionid` int(11) NOT NULL AUTO_INCREMENT,
  `question_info` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `topicid` int(11) NOT NULL COMMENT '0 注册',
  `answer_field` varchar(64) NOT NULL,
  `proc_func` varchar(64) NOT NULL,
  `proc_module` varchar(64) NOT NULL,
  PRIMARY KEY (`questionid`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

CREATE TABLE `pa_message_t_modules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cur_questionid` int(11) NOT NULL,
  `next_questionid` int(11) NOT NULL,
  `cur_value` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

CREATE TABLE `pa_message_t_messages` (
  `messageid` int(11) NOT NULL AUTO_INCREMENT,
  `messageinfo` varchar(2000) NOT NULL,
  `questionid` int(11) NOT NULL,
  `time` time NOT NULL,
  `userid` int(11) NOT NULL,
  PRIMARY KEY (`messageid`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

CREATE TABLE `pa_message_t_user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `createtime` time NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;