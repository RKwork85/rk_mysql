// data = {
//     "data1": "一、直播讲解",
//     "data2": "功能视频"
//   }

// data1: 
// 一、直播讲解
// 二、品牌营销
// data2:
// 功能视频
// 场景视频
// 穿搭视频
// 痛点视频



function main({ data1, data2 }) {
    // 定义前缀和后缀的映射关系
    const prefixMap = {
        "功能视频": "Functional_Videos",
        "场景视频": "Scene_Videos",
        "穿搭视频": "Outfit_Videos",
        "痛点视频": "Pain_Point_Videos"
    };

    const suffixMap = {
        "一、直播讲解": "_Explanation",
        "二、品牌营销": "_Marketing"
    };

    // 获取对应的前缀和后缀
    const prefix = prefixMap[data2];
    const suffix = suffixMap[data1];

    // 检查输入是否有效
    if (!prefix) {
        throw new Error(`无效的 data2 值: ${data2}`);
    }
    if (!suffix) {
        throw new Error(`无效的 data1 值: ${data1}`);
    }

    // 拼接表名
    const tableName = prefix + suffix;

    // 返回结果
    return { Template_table_name: tableName };
}

// 测试函数
const data = {
    data1: "二、品牌营销",
    data2: "功能视频"
};

console.log(main(data));  // 输出：{ Template_table_name: "Functional_Videos_Explanation" }