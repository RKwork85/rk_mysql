function main({data1}) {
    // 提取字符串中 JSON 内容的起始和结束位置
    const jsonStart = data1.indexOf('{');
    const jsonEnd = data1.lastIndexOf('}') + 1;

    // 使用字符串切割函数从原字符串中提取 JSON 部分
    const jsonString = data1.substring(jsonStart, jsonEnd);

    // 解析 JSON 字符串成 JavaScript 对象
    const jsonObject = JSON.parse(jsonString);

    // 为每个 JSON 键赋予对应的变量
    const {
        品牌: brand,
        产品: product,
        颜色: colors,
        工艺: process,
        用户痛点: userPainPoints,
        运动场景: sportScenes,
        'FAB 产品解说': fabProductDescription,
        面料解说: fabricDescription,
        一句话宣传: tagline,
        面料宣传: fabricTagline,
        版型宣传: patternTagline,
        设计宣传: designTagline
    } = jsonObject;

    // 重新构造一个新对象，用于返回
     return{
        brand,
        product,
        colors,
        process,
        userPainPoints,
        sportScenes,
        fabProductDescription,
        fabricDescription,
        tagline,
        fabricTagline,
        patternTagline,
        designTagline
    };
}



data = {data1:`{
    "品牌": "132",
    "产品": "",
    "颜色": "",
    "工艺": "",
    "用户痛点": "",
    "运动场景": "",
    "FAB产品解说": "",
    "面料解说": "",
    "一句话宣传": "",
    "面料宣传": "",
    "版型宣传": "",
    "设计宣传": ""
  }`
}
  console.log(main(data))