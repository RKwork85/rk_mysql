const data = {
    "data1": "{\"result\":[{\"ID\":20,\"Product_FabDescription\":\"优雅的 U 形领设计，兼具时尚与功能，为锁骨赋予完美曲线。\",\"Tag\":\"FAB 产品解说\",\"Card\":5},{\"ID\":21,\"Product_FabDescription\":\"后开扣设计让穿脱更便捷，特别适合日常练习需要频繁更换的用户。\",\"Tag\":\"FAB 产品解说\",\"Card\":5},{\"ID\":22,\"Product_FabDescription\":\"高弹性面料，提升舒适度，运动更放心不移位。\",\"Tag\":\"FAB 产品解说\",\"Card\":5},{\"ID\":23,\"Product_FabDescription\":\"提高包裹性的侧翼设计，稳定控制副乳，告别运动中多余的晃动。\",\"Tag\":\"FAB 产品解说\",\"Card\":5},{\"ID\":9,\"Product_FabDescription\":\"高科技面料组合，柔软贴合如第二层肌肤，完美适应极速运动状况。\",\"Tag\":\"面料宣传\",\"Card\":5},{\"ID\":10,\"Product_FabDescription\":\"卓越的抗撕拉能力与耐用性，确保每一次运动都充满活力与自信。\",\"Tag\":\"面料宣传\",\"Card\":5},{\"ID\":5,\"Product_FabDescription\":\"净色\",\"Tag\":\"工艺\",\"Card\":5},{\"ID\":17,\"Product_FabDescription\":\"跑步\",\"Tag\":\"运动场景\",\"Card\":5},{\"ID\":18,\"Product_FabDescription\":\"器械训练\",\"Tag\":\"运动场景\",\"Card\":5},{\"ID\":19,\"Product_FabDescription\":\"跳绳\",\"Tag\":\"运动场景\",\"Card\":5},{\"ID\":20,\"Product_FabDescription\":\"拳击\",\"Tag\":\"运动场景\",\"Card\":5},{\"ID\":5,\"Product_FabDescription\":\"现代女性运动必备，塑形、舒适、方便的完美结合！\",\"Tag\":\"一句话宣传\",\"Card\":5},{\"ID\":15,\"Product_FabDescription\":\"不易找到既塑形又舒适的内衣，后开扣设计解决穿脱不便的问题\",\"Tag\":\"用户痛点\",\"Card\":5},{\"ID\":16,\"Product_FabDescription\":\"需要在运动时能有效控制震动，立体胸型设计带来稳定缓震效果\",\"Tag\":\"用户痛点\",\"Card\":5},{\"ID\":17,\"Product_FabDescription\":\"渴望在运动中保持干燥及清爽，一体式固定杯与速干面料助力自由运动\",\"Tag\":\"用户痛点\",\"Card\":5},{\"ID\":18,\"Product_FabDescription\":\"希望内衣耐磨、耐洗，并能保持形状，净色工艺和高弹性能提供此体验\",\"Tag\":\"用户痛点\",\"Card\":5},{\"ID\":5,\"Product_FabDescription\":\"紧身 修身 合体 宽松, 多种版型，精准裁剪与科学设计，确保每一件都仿佛为您量身定制，带来无与伦比的穿着体验。\",\"Tag\":\"版型宣传\",\"Card\":5},{\"ID\":17,\"Product_FabDescription\":\"U 形领口完美显露锁骨，提升整体优雅气质。\",\"Tag\":\"设计宣传\",\"Card\":5},{\"ID\":18,\"Product_FabDescription\":\"后开扣设计更便于穿脱，为运动生活增添细节贴心。\",\"Tag\":\"设计宣传\",\"Card\":5},{\"ID\":19,\"Product_FabDescription\":\"一体式固定杯，辅以高弹性包边，确保激烈运动中保持稳定。\",\"Tag\":\"设计宣传\",\"Card\":5},{\"ID\":20,\"Product_FabDescription\":\"侧翼加高设计，增强包裹性，运动时轻松应对震动，给您最安心的体验。\",\"Tag\":\"设计宣传\",\"Card\":5},{\"ID\":18,\"Product_FabDescription\":\"75%锦纶与 25%氨纶混纺，带来最佳的光滑触感与弹性。\",\"Tag\":\"面料解说\",\"Card\":5},{\"ID\":19,\"Product_FabDescription\":\"材料经过多重工艺处理，确保出汗时也能维持面料的舒适干爽。\",\"Tag\":\"面料解说\",\"Card\":5}]}",
    "data2": "浅象牙"
};

function main({ data1, data2 }) {
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
            groupedData[tag] = [];
        }

        // 将当前项的 Product_FabDescription 添加到对应的 Tag 数组
        groupedData[tag].push(productDescription);
    });

    // 提取结果到一个二维数组
    const resultList = Object.entries(groupedData).map(([tag, descriptions]) => [tag, ...descriptions]);

    // 定义每个二维数组对应的选取条数
    const selectionCounts = [
        2,    // index 0 :FAB 产品解说
        1,    // index 1:面料宣传
        1,    // index 2:工艺
        2,    // index 3：运动场景
        1,    // index 4：一句话宣传
        1,    // index 5：用户痛点
        1,    // index 6：版型宣传
        2,    // index 7：设计宣传
        1,    // index 8：面料解说
    ];

    // 创建一个函数来处理随机选择
    function selectRandomItems(array, count) {
        if (Array.isArray(count)) {
            // 随机选择 count 中的一个值
            count = count[Math.floor(Math.random() * count.length)];
        }
        const shuffled = array.slice(); // 复制数组
        shuffled.sort(() => 0.5 - Math.random());
        return shuffled.slice(0, count);
    }

    // 使用随机选择逻辑选择结果
    const finalResult = resultList.map((subArray, index) => {
        const chosenItems = selectRandomItems(subArray.slice(1), selectionCounts[index]);
        return `${subArray[0]}: ${chosenItems.join(', ')}`;
    });

    // 以 \n 连接结果
    const dataStr = finalResult.join('\n');
    let randomNum = Math.random();
    let outputStr = '';

    // 判断随机数是否大于0.5，从而决定输出结果
    if (randomNum >= 0.5) {
        outputStr = dataStr + '\n' + `颜色：${data2}`;
    } else {
        outputStr = dataStr + '\n' + "无颜色";
    }

    // 返回结果格式
    return { productInput: outputStr };
}

console.log(main(data));