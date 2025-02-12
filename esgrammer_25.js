function generateProductDisplay(input) {
    const output = {
        "整体画面": {
            "模特展示": ["静态展示", "动态展示"],
            "产品展示": ["悬挂展示", "平铺展示", "对比展示"]
        },
        "产品细节画面": {
            "产品展示": input["产品细节"],
            "模特展示": input["产品细节"]
        },
        "产品体验画面": input["产品体验"],
        "产品功能画面": input["产品功能"],
        "产品风格画面": input["产品风格"],
        "产品运动场景画面": input["产品运动场景"]
    };
    return output;
}

// 示例输入
const input ={
    "产品细节": ["U形领", "后开扣", "一体式固定杯", "侧翼加高"],
    "产品体验": ["光滑触感", "柔软贴合", "舒适"],
    "产品功能": ["塑形", "稳定缓震", "控制副乳", "速干", "耐磨耐洗", "保持形状"],
    "产品风格": ["时尚风"],
    "产品运动场景": ["跑步", "器械训练", "跳绳", "拳击"]
    } ;

// 生成输出
const output = generateProductDisplay(input);
console.log(output);

function printFolderTree(data, level = 0) {
    const indent = "│   ".repeat(level); // 每一层缩进

    for (const key in data) {
        if (data.hasOwnProperty(key)) {
            // 打印文件夹名
            if (level === 0) {
                console.log(`${key}`); // 根目录不缩进
            } else {
                console.log(`${indent}├── ${key}`);
            }

            // 如果值是数组，打印数组内容
            if (Array.isArray(data[key])) {
                data[key].forEach((item, index) => {
                    const isLast = index === data[key].length - 1;
                    const branch = isLast ? "    " : "│   ";
                    console.log(`${indent}${branch}├── ${item}`);
                });
            } else if (typeof data[key] === "object" && data[key] !== null) {
                // 如果值是对象，递归打印子文件夹
                printFolderTree(data[key], level + 1);
            }
        }
    }
}
printFolderTree(output);