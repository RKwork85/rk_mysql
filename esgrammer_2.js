function getTopicEnglish(str) {
  const topicMap = {
    '日常话题': 'Daily_Topics',
    '风格话题': 'Style_Topics',
    '场景话题': 'Scene_Topics',
    '功能话题': 'Function_Topics',
    '好物话题': 'Good_Finds_Topics',
    '个性话题': 'Personality_Topics'
  };

  // 查找对应的英文内容
  const englishTopic = topicMap[str];

  // 返回格式 {table: 英文字符串}
  if (englishTopic) {
    return { table: englishTopic };
  } else {
    return { table: 'Topic not found' };
  }
}

// 示例用法
console.log(getTopicEnglish('日常话题')); // 输出: { table: 'Daily_Topics' }
console.log(getTopicEnglish('风格话题')); // 输出: { table: 'Style_Topics' }
console.log(getTopicEnglish('场景话题')); // 输出: { table: 'Scene_Topics' }
console.log(getTopicEnglish('功能话题')); // 输出: { table: 'Function_Topics' }
console.log(getTopicEnglish('好物话题')); // 输出: { table: 'Good_Finds_Topics' }
console.log(getTopicEnglish('个性话题')); // 输出: { table: 'Personality_Topics' }
console.log(getTopicEnglish('其他话题')); // 输出: { table: 'Topic not found' }


{
  "result": "{\"result\":[{\"Product_ID\":1,\"Product_Name\":\"小冰纱防晒外套\",\"brand_id\":1},{\"Product_ID\":2,\"Product_Name\":\"无缝拼接鹅绒外套\",\"brand_id\":1}]}"
}