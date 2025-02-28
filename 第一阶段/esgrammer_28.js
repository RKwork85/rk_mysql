function processData(data, userSelectColor) {
    // 解析 JSON 数据
    const parsedData = JSON.parse(data.data1).result;

    // 创建一个对象用于存储处理后的结果
    const result = {};

    // 遍历数据，按照 Tag 分组并合并 Product_FabDescription
    parsedData.forEach(item => {
        const tag = item.Tag;
        const description = item.Product_FabDescription;

        // 如果当前 Tag 不存在于 result 中，则初始化为空数组
        if (!result[tag]) {
            result[tag] = [];
        }

        // 将当前描述添加到对应 Tag 的数组中
        result[tag].push(description);
    });

    // 处理颜色逻辑
    console.log(result)
    result["颜色"] = []
    result["颜色"].push(userSelectColor)

    // 将每个 Tag 对应的数组转换为字符串，用换行符分隔，并添加缩进
    const processedResult = Object.keys(result).map(tag => {
        const descriptions = result[tag].map(desc => `    ${desc}`).join('\n'); // 每条内容缩进4个空格
        return `${tag}：\n${descriptions}`;
    }).join('\n\n'); // 每个 Tag 之间用两个换行符分隔

    // 返回最终结果
    return { result: processedResult };
}

// 测试数据
const data = {
    "data1": "{\"result\":[{\"ID\":12,\"Product_FabDescription\":\"具有法式松弛感。展现出从容自在的休闲风格。让您在日常中轻松拿捏休闲姿态，彰显独特魅力。\",\"Tag\":\"FAB 产品解说\",\"Card\":3},{\"ID\":13,\"Product_FabDescription\":\"优雅小圆领。巧妙地露出锁骨，增添女性魅力。使您更具女人味，展现迷人风采。\",\"Tag\":\"FAB 产品解说\",\"Card\":3},{\"ID\":14,\"Product_FabDescription\":\"合身小短款。修饰身材，显腿长。帮助您优化身材比例，展现更好的身形。\",\"Tag\":\"FAB 产品解说\",\"Card\":3},{\"ID\":15,\"Product_FabDescription\":\"100%绵羊毛面料。手感细腻柔滑，亲肤舒适。为您带来极佳的穿着体验，享受舒适与温暖。\",\"Tag\":\"FAB 产品解说\",\"Card\":3},{\"ID\":5,\"Product_FabDescription\":\"100%绵羊毛，亲肤柔软，给您温暖呵护。\",\"Tag\":\"面料宣传\",\"Card\":3},{\"ID\":6,\"Product_FabDescription\":\"精选优质绵羊毛，细腻柔滑，畅享舒适体验。\",\"Tag\":\"面料宣传\",\"Card\":3},{\"ID\":3,\"Product_FabDescription\":\"净色\",\"Tag\":\"工艺\",\"Card\":3},{\"ID\":10,\"Product_FabDescription\":\"日常\",\"Tag\":\"运动场景\",\"Card\":3},{\"ID\":11,\"Product_FabDescription\":\"休闲\",\"Tag\":\"运动场景\",\"Card\":3},{\"ID\":12,\"Product_FabDescription\":\"网球\",\"Tag\":\"运动场景\",\"Card\":3},{\"ID\":3,\"Product_FabDescription\":\"100%绵羊毛，自带慵懒法式感！\",\"Tag\":\"一句话宣传\",\"Card\":3},{\"ID\":7,\"Product_FabDescription\":\"渴望拥有一件能够展现独特风格和品味的羊毛开衫。\",\"Tag\":\"用户痛点\",\"Card\":3},{\"ID\":8,\"Product_FabDescription\":\"担心羊毛开衫的穿着舒适度不够。\",\"Tag\":\"用户痛点\",\"Card\":3},{\"ID\":9,\"Product_FabDescription\":\"希望羊毛开衫的款式能够修饰身材，展现出更好的效果。\",\"Tag\":\"用户痛点\",\"Card\":3},{\"ID\":10,\"Product_FabDescription\":\"想要一件能够适应多种场合穿搭的羊毛开衫。\",\"Tag\":\"用户痛点\",\"Card\":3},{\"ID\":3,\"Product_FabDescription\":\"宽松版型，自在舒适，尽显随性魅力。\",\"Tag\":\"版型宣传\",\"Card\":3},{\"ID\":9,\"Product_FabDescription\":\"奶白色\",\"Tag\":\"颜色\",\"Card\":3},{\"ID\":10,\"Product_FabDescription\":\"花灰色\",\"Tag\":\"颜色\",\"Card\":3},{\"ID\":11,\"Product_FabDescription\":\"迪奥粉\",\"Tag\":\"颜色\",\"Card\":3},{\"ID\":12,\"Product_FabDescription\":\"铁锈红\",\"Tag\":\"颜色\",\"Card\":3},{\"ID\":13,\"Product_FabDescription\":\"铁摩咖\",\"Tag\":\"颜色\",\"Card\":3},{\"ID\":14,\"Product_FabDescription\":\"深邃黑\",\"Tag\":\"颜色\",\"Card\":3},{\"ID\":9,\"Product_FabDescription\":\"法式慵懒风设计，演绎浪漫随性的时尚态度。\",\"Tag\":\"设计宣传\",\"Card\":3},{\"ID\":10,\"Product_FabDescription\":\"优雅小圆领设计，展现迷人锁骨线条。\",\"Tag\":\"设计宣传\",\"Card\":3},{\"ID\":11,\"Product_FabDescription\":\"下摆袖口细密罗纹设计，增加细节美感与保暖性。\",\"Tag\":\"设计宣传\",\"Card\":3},{\"ID\":12,\"Product_FabDescription\":\"纽扣开衫设计，灵活多变，满足不同穿搭需求。\",\"Tag\":\"设计宣传\",\"Card\":3},{\"ID\":10,\"Product_FabDescription\":\"面料采用 100%绵羊毛，具有优异的柔软性。\",\"Tag\":\"面料解说\",\"Card\":3},{\"ID\":11,\"Product_FabDescription\":\"100%绵羊毛材质，使开衫具有良好的保暖性能。\",\"Tag\":\"面料解说\",\"Card\":3},{\"ID\":12,\"Product_FabDescription\":\"绵羊毛面料细腻柔滑，肌肤触感极佳。\",\"Tag\":\"面料解说\",\"Card\":3},{\"ID\":13,\"Product_FabDescription\":\"优质的绵羊毛，保证了开衫的品质和耐用性。\",\"Tag\":\"面料解说\",\"Card\":3}]}"
};

// 调用函数并打印结果
const processedData = processData(data, "青色");
console.log(processedData.result);