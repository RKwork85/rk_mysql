let result = {
  "result":"{\"result\":[{\"ID\":16,\"Product_FabDescription\":\"衣橱必备款，多场景适用。满足不同场合的穿着需求。让您轻松应对各种活动，无需为穿搭烦恼。\",\"Tag\":\"FAB 产品解说\",\"Card\":4},{\"ID\":17,\"Product_FabDescription\":\"立领连帽设计。有效抵御寒风。为您提供温暖的保护，增强舒适感。\",\"Tag\":\"FAB 产品解说\",\"Card\":4},{\"ID\":18,\"Product_FabDescription\":\"立体剪裁。完美贴合身形。能够勾勒出曼妙曲线，展现您的好身材。\",\"Tag\":\"FAB 产品解说\",\"Card\":4},{\"ID\":19,\"Product_FabDescription\":\"修身后腰设计。进一步凸显身材优势。让您看起来更加苗条，增强自信心。\",\"Tag\":\"FAB 产品解说\",\"Card\":4},{\"ID\":7,\"Product_FabDescription\":\"优质面料，吸湿排汗，让您时刻保持干爽舒适。\",\"Tag\":\"面料宣传\",\"Card\":4},{\"ID\":8,\"Product_FabDescription\":\"磨毛印花面料，时尚与舒适兼得。\",\"Tag\":\"面料宣传\",\"Card\":4},{\"ID\":4,\"Product_FabDescription\":\"印花\",\"Tag\":\"工艺\",\"Card\":4},{\"ID\":13,\"Product_FabDescription\":\"日常\",\"Tag\":\"运动场景\",\"Card\":4},{\"ID\":14,\"Product_FabDescription\":\"休闲\",\"Tag\":\"运动场景\",\"Card\":4},{\"ID\":15,\"Product_FabDescription\":\"网球\",\"Tag\":\"运动场景\",\"Card\":4},{\"ID\":16,\"Product_FabDescription\":\"跳绳\",\"Tag\":\"运动场景\",\"Card\":4},{\"ID\":4,\"Product_FabDescription\":\"衣橱必备款，逛街运动两不误的全能外套！\",\"Tag\":\"一句话宣传\",\"Card\":4},{\"ID\":11,\"Product_FabDescription\":\"期望找到一件在多种场景都能穿着的外套。\",\"Tag\":\"用户痛点\",\"Card\":4},{\"ID\":12,\"Product_FabDescription\":\"担心外套的保暖性不够好。\",\"Tag\":\"用户痛点\",\"Card\":4},{\"ID\":13,\"Product_FabDescription\":\"想要一件能够展现身材优势的外套。\",\"Tag\":\"用户痛点\",\"Card\":4},{\"ID\":14,\"Product_FabDescription\":\"希望外套的面料既美观又舒适。\",\"Tag\":\"用户痛点\",\"Card\":4},{\"ID\":4,\"Product_FabDescription\":\"修身版型，展现完美身材曲线。\",\"Tag\":\"版型宣传\",\"Card\":4},{\"ID\":13,\"Product_FabDescription\":\"时尚百搭风设计，轻松搭配各种服饰。\",\"Tag\":\"设计宣传\",\"Card\":4},{\"ID\":14,\"Product_FabDescription\":\"立体分割线设计，增加视觉层次感。\",\"Tag\":\"设计宣传\",\"Card\":4},{\"ID\":15,\"Product_FabDescription\":\"立领连帽设计，防风保暖又时尚。\",\"Tag\":\"设计宣传\",\"Card\":4},{\"ID\":16,\"Product_FabDescription\":\"防风袖套设计，提供额外的防护。\",\"Tag\":\"设计宣传\",\"Card\":4},{\"ID\":14,\"Product_FabDescription\":\"面料成分包含 75%锦纶和 25%氨纶，具有良好的弹性。\",\"Tag\":\"面料解说\",\"Card\":4},{\"ID\":15,\"Product_FabDescription\":\"磨毛印花面料，图案精美，增添时尚感。\",\"Tag\":\"面料解说\",\"Card\":4},{\"ID\":16,\"Product_FabDescription\":\"面料具有吸湿排汗功能，保持身体干爽。\",\"Tag\":\"面料解说\",\"Card\":4},{\"ID\":17,\"Product_FabDescription\":\"亲肤舒适的面料，让您穿着无不适感。\",\"Tag\":\"面料解说\",\"Card\":4}]}"
}

function main({ result }) {
  // 解析 JSON 字符串
  const parsedData = JSON.parse(result);

  // 获取 'result' 数组
  const resultArray = parsedData.result;

  // 创建一个对象用于根据 Tag 分组数据
  const groupedData = {};

  // 遍历 resultArray
  resultArray.forEach(item => {
      const tag = item.Tag;
      const productDescription = item.Product_FabDescription;
      console.log(productDescription)

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
      2,    // index 0 :FAB 产品解说
      1,    // index 1:面料宣传
      [1, 0], // index 2:工艺
      [2, 1], // index 3：运动场景
      [1, 0], // index 4：一句话宣传
      [1, 0], // index 5：用户痛点
      [1, 0], // index 6：版型宣传
      [1, 3], // index 7：设计宣传
      [1, 0], // index 8：面料解说
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
  let randomNum = Math.random();
  let outputStr =''
  // 判断随机数是否大于0.5，从而决定输出结果
  if (randomNum >= 0.5) {

      
  } else {
      console.log("无颜色");
  }
  // 返回结果格式
  return { productInput: dataStr };
}

output = main(result)
console.log(output.productInput)