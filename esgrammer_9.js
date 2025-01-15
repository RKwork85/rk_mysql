data ={
    "result": "{\"result\":[{\"ID\":1,\"Product_FabDescription\":\"低领短帽檐设计，方便穿戴，不勒脖子\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"立体宽松 H 裁剪，友好兼容不同身形\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"后开马尾孔设计，第二橡皮筋，发型不凌乱\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"软帽檐设计，随意折叠,轻量遮阳\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":5,\"Product_FabDescription\":\"加长勾手袖子，防晒至手背，袖子不上跑\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":6,\"Product_FabDescription\":\"两侧插袋，能放方便置纳物件\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":7,\"Product_FabDescription\":\"下脚可调节扣，自由收口及松放，不让风钻空子\",\"Tag\":\"产品解说\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"原纱型防晒 UPF50+，硬核型物理防晒，有效阻隔紫外线，同时水洗也不减防晒力；\",\"Tag\":\"面料宣传\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"水洗也不减防晒力；\",\"Tag\":\"面料宣传\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"净色\",\"Tag\":\"工艺\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"户外\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"跑步\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"休闲日常\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"网球\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":5,\"Product_FabDescription\":\"骑行\",\"Tag\":\"运动场景\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"一体式冰感包裹，挡住紫外线，体感冰凉，化身肌肤“遮阳伞、保护壳”，令你住进清凉里，肌肤水润依旧\",\"Tag\":\"一句话宣传\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"①想要一件防晒值高的百搭防晒外套；\",\"Tag\":\"用户痛点\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"②最好上身不闷汗、还清凉功能：防晒\",\"Tag\":\"用户痛点\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"版型：宽松款，包容不同身材，藏肉显瘦尺码：\",\"Tag\":\"版型宣传\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"冰川白\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"浅茶杏\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"冰川灰\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"曜石黑\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":5,\"Product_FabDescription\":\"海沫绿\",\"Tag\":\"颜色\",\"Card\":1},{\"ID\":1,\"Product_FabDescription\":\"风格设计:简约百搭风，轻松搭遍万物，1 件当 8 件穿，跑步、网球、徒步、爬山等运动与日常休闲都可穿\",\"Tag\":\"设计宣传\",\"Card\":1},{\"ID\":2,\"Product_FabDescription\":\"下摆设计:下摆带抽绳，可调节，收紧、放松状态适配运动、休闲场景\",\"Tag\":\"设计宣传\",\"Card\":1},{\"ID\":3,\"Product_FabDescription\":\"帽子设计:软帽檐设计，防晒也不影响造型，收纳折叠不变形；帽子后方自带马尾孔，清爽透气、也不乱发型\",\"Tag\":\"设计宣传\",\"Card\":1},{\"ID\":4,\"Product_FabDescription\":\"袖子设计:加长袖子设计，防晒至手背，同时固定袖子，动起来不跑位不上窜\",\"Tag\":\"设计宣传\",\"Card\":1}]}"
  }


  function main({result}) {
    const data = JSON.parse(result)
    const dataList = data.result

    dataList.forEach(item =>{
        console.log(item)
    })

  }

  main(data)



  // 产品解说：
  // 工艺：
  // 面料宣传：
  // 运动场景：
  // 一句话宣传：
  // 版型宣传：
  // 用户痛点：
  // 颜色：
  // 设计宣传：
  
