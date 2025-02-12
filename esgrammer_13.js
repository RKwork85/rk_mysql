function main({ data1, data2, data3 }) {
    // 给每个 data1 元素添加 productNumber 和AIresponse
    const updatedDataList = data1.map((item, index) => ({
        ...item,
        productNumber: data3,  // 假设 data3 的长度和 data1 的长度是相同的
        AIresponse: data2[index]       // data2 也是按相同顺序添加
    }));
    
    // 生成 Markdown 表格
    let mdTable = '| 产品编号 | 模板编号 | 文案内容 |\n';
    mdTable += '| -------- | -------- | -------- |\n'; // 表头下方的分隔线

    updatedDataList.forEach(item => {
        mdTable += `| ${item.productNumber} | ${item.ID} | ${item.Template} |\n`;
    });

    console.log(mdTable); // 输出 Markdown 表格
    return {
        result: updatedDataList
    };
}

// 示例数据
const data1 = [
    {
        ID: 1,
        Template: '终于把速惟家的这件羊毛开衫价格打下来了。真的超级暖和，100%的羊毛，非常轻薄，一点都不显臃肿，对身材的包容性很高。微胖的姐妹也能穿，直接去冲！'
    },
    {
        ID: 2,
        Template: '这款 100%的羊毛开衫真的绝了！这样叠穿也非常好看。袖子做了一个超流行的超长插袖，显得整个手臂非常修长。上身就是一个三七分，非常显身材，喜欢的姐妹赶紧去冲！'
    },
    {
        ID: 3,
        Template: '这件真不贵啦！花线衣的价格买到 100%的羊毛！肩线都是这种正边的版型，每个颜色都好好看。特别是这个粉色，真的超减龄，搭休闲裤、牛仔裤、长裙、短裙都很好看！'
    }
];

const data2 = ['hhh', 'lll', 'nnn'];
const data3 = 'sdasdasd';  // 假设 data3 的内容

// 调用 main 函数
main({ data1, data2, data3 });
