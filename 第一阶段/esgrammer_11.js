function main({ data1 }) {
    // 解析 JSON 字符串
    const parsedData = JSON.parse(data1);
  
    // 获取 'result' 数组
    const resultArray = parsedData.result;
  
    // 创建一个对象用于根据 Tag 分组数据
    const groupedData = {};
  
    // 遍历 resultArray
    resultArray.forEach(item => {
        const tag = item.Tag;
        const productDescription = item.Product_FabDescription;

        // 如果还没有此 Tag 的记录，则初始化一个数组
        if (!groupedData[tag]) {
            groupedData[tag] = [tag];
        }
        
        // 将当前项的 Product_FabDescription 添加到对应的 Tag 数组
        groupedData[tag].push(productDescription);
    });
  
    // 提取结果到一个二维数组
    const resultList = Object.values(groupedData);
  
    // 定义每个二维数组对应的选取条数
    const selectionCounts = [
        2,    // index 0 产品解说
        1,    // index 1 面料宣传
        [1, 0], // index 2  工艺
        [2, 1], // index 3 运动场景
        [1, 0], // index 4  一句话宣传
        [1, 0], // index 5  用户痛点
        [1, 0], // index 6  版型宣传
        [1, 3], // index 7  颜色
        [1, 2], // index 8  设计宣传
        1     // index 9  面料解说
    ];
  
    // 创建一个函数来处理随机选择
    function selectRandomItems(array, count) {
        if (Array.isArray(count)) {
            // 随机选择 count 中的一个值
            count = count[Math.floor(Math.random() * count.length)];
        }
        const shuffled = array.slice(1); // 去掉第一个元素
        shuffled.sort(() => 0.5 - Math.random());
        return shuffled.slice(0, count);
    }
  
    // 使用随机选择逻辑选择结果
    const finalResult = resultList.map((subArray, index) => {
        const chosenItems = selectRandomItems(subArray, selectionCounts[index]);
        return `${subArray[0]}: ${chosenItems.join(', ')}`;
    });
  
    // 以 \n 连接结果
    const dataStr = finalResult.join('\n');

    // 返回结果格式
    return { input: dataStr };
}
  
  let data = {
    "data1": "{\"result\":[{\"ID\":1,\"Product_FabDescription\":\"低领短帽檐设计，方便穿戴，不勒脖子\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"立体宽松 H 裁剪，友好兼容不同身形\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"后开马尾孔设计，第二橡皮筋，发型不凌乱\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"软帽檐设计，随意折叠,轻量遮阳\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":5,\"Product_FabDescription\":\"加长勾手袖子，防晒至手背，袖子不上跑\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":6,\"Product_FabDescription\":\"两侧插袋，能放方便置纳物件\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":7,\"Product_FabDescription\":\"下脚可调节扣，自由收口及松放，不让风钻空子\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"原纱型防晒 UPF50+，硬核型物理防晒，有效阻隔紫外线，同时水洗也不减防晒力；\",\"Tag\":\"面料宣传\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"水洗也不减防晒力；\",\"Tag\":\"面料宣传\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"净色\",\"Tag\":\"工艺\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"户外\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"跑步\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"休闲日常\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"网球\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":5,\"Product_FabDescription\":\"骑行\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"一体式冰感包裹，挡住紫外线，体感冰凉，化身肌肤“遮阳伞、保护壳”，令你住进清凉里，肌肤水润依旧\",\"Tag\":\"一句话宣传\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"①想要一件防晒值高的百搭防晒外套；\",\"Tag\":\"用户痛点\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"②最好上身不闷汗、还清凉功能：防晒\",\"Tag\":\"用户痛点\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"版型：宽松款，包容不同身材，藏肉显瘦尺码：\",\"Tag\":\"版型宣传\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"冰川白\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"浅茶杏\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"冰川灰\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"曜石黑\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":5,\"Product_FabDescription\":\"海沫绿\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"风格设计:简约百搭风，轻松搭遍万物，1 件当 8 件穿，跑步、网球、徒步、爬山等运动与日常休闲都可穿\",\"Tag\":\"设计宣传\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"下摆设计:下摆带抽绳，可调节，收紧、放松状态适配运动、休闲场景\",\"Tag\":\"设计宣传\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"帽子设计:软帽檐设计，防晒也不影响造型，收纳折叠不变形；帽子后方自带马尾孔，清爽透气、也不乱发型\",\"Tag\":\"设计宣传\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"袖子设计:加长袖子设计，防晒至手背，同时固定袖子，动起来不跑位不上窜\",\"Tag\":\"设计宣传\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"原纱型硬核物理防晒，高倍抗光老\",\"Tag\":\"面料解说\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"水柔原纱，越穿越凉快\",\"Tag\":\"面料解说\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"吸湿速干，汗水迅速蒸发，凉爽透气不变形\",\"Tag\":\"面料解说\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"轻盈挺阔，出汗不粘身\",\"Tag\":\"面料解说\",\"Card\":1}]}"
  }  
  let result_list = main(data);
  
  console.log(result_list)
  console.log(result_list.length)



//   [
//     [
//       "产品解说",
//       "低领短帽檐设计，方便穿戴，不勒脖子",
//       "立体宽松 H 裁剪，友好兼容不同身形",
//       "后开马尾孔设计，第二橡皮筋，发型不凌乱",
//       "软帽檐设计，随意折叠,轻量遮阳",
//       "加长勾手袖子，防晒至手背，袖子不上跑",
//       "两侧插袋，能放方便置纳物件",
//       "下脚可调节扣，自由收口及松放，不让风钻空子"
//     ],
//     [
//       "面料宣传",
//       "原纱型防晒 UPF50+，硬核型物理防晒，有效阻隔紫外线，同时水洗也不减防晒力；",
//       "水洗也不减防晒力；"
//     ],
//     [
//       "工艺",
//       "净色"
//     ],
//     [
//       "运动场景",
//       "户外",
//       "跑步",
//       "休闲日常",
//       "网球",
//       "骑行"
//     ],
//     [
//       "一句话宣传",
//       "一体式冰感包裹，挡住紫外线，体感冰凉，化身肌肤“遮阳伞、保护壳”，令你住进清凉里，肌肤水润依旧"
//     ],
//     [
//       "用户痛点",
//       "①想要一件防晒值高的百搭防晒外套；",
//       "②最好上身不闷汗、还清凉功能：防晒"
//     ],
//     [
//       "版型宣传",
//       "版型：宽松款，包容不同身材，藏肉显瘦尺码："
//     ],
//     [
//       "颜色",
//       "冰川白",
//       "浅茶杏",
//       "冰川灰",
//       "曜石黑",
//       "海沫绿"
//     ],
//     [
//       "设计宣传",
//       "风格设计:简约百搭风，轻松搭遍万物，1 件当 8 件穿，跑步、网球、徒步、爬山等运动与日常休闲都可穿",
//       "下摆设计:下摆带抽绳，可调节，收紧、放松状态适配运动、休闲场景",
//       "帽子设计:软帽檐设计，防晒也不影响造型，收纳折叠不变形；帽子后方自带马尾孔，清爽透气、也不乱发型",
//       "袖子设计:加长袖子设计，防晒至手背，同时固定袖子，动起来不跑位不上窜"
//     ],
//     [
//       "面料解说",
//       "原纱型硬核物理防晒，高倍抗光老",
//       "水柔原纱，越穿越凉快",
//       "吸湿速干，汗水迅速蒸发，凉爽透气不变形",
//       "轻盈挺阔，出汗不粘身",
//       "原纱型硬核物理防晒，高倍抗光老"
//     ]
//   ]