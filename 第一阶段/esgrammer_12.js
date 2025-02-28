// 输出的内容

const data ={
    "result": "{\"result\":[{\"ID\":1,\"Template\":\"终于把速惟家的这件羊毛开衫价格打下来了。真的超级暖和，100%的羊毛，非常轻薄，一点都不显臃肿，对身材的包容性很高。微胖的姐妹也能穿，直接去冲！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":2,\"Template\":\"这款 100%的羊毛开衫真的绝了！这样叠穿也非常好看。袖子做了一个超流行的超长插袖，显得整个手臂非常修长。上身就是一个三七分，非常显身材，喜欢的姐妹赶紧去冲！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":3,\"Template\":\"这件真不贵啦！花线衣的价格买到 100%的羊毛！肩线都是这种正边的版型，每个颜色都好好看。特别是这个粉色，真的超减龄，搭休闲裤、牛仔裤、长裙、短裙都很好看！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":4,\"Template\":\"很有调性的羊毛开衫，出门不知道怎么搭配的姐妹，你可以内搭一件小背心，外穿一条休闲裤，就很好看。还在纠结颜色的姐妹，听我的，直接入手我身上这个颜色，喜欢的姐妹赶紧去冲！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":5,\"Template\":\"版型很好，性价比高。花线衣的价格买到 100%的羊毛！不挑身材、不挑款式的基础版，怎么穿搭都不会出错。肩线都是这种正边的版型。不是收腰的，它偏慵懒，上身就是一个三七分！真的很爱！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":6,\"Template\":\"年货节上新的这件羊毛开衫，真的太好看啦！整个肩线都是这种正边的版型，上身就是一个三七分，非常显身材。搭休闲裤、牛仔裤、长裙、短裙都很好看！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":7,\"Template\":\"准备开春啦！这件羊毛开衫必须要有一件！无论你穿到任何场合，都不会突兀。肩线都是这种正边的版型，不是收腰的，它偏慵懒，上身就是一个三七分，识货的姐妹赶紧入手！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":8,\"Template\":\"版型很经典，高矮胖瘦都合适，不挑人。 100%的羊毛，深冬开春都可以穿。重点是颜色真的好好看啊！推荐入手铁锈红！过年回家给自己带一件，妈妈带一件！再不入手就来不及啦！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":9,\"Template\":\"你去留意一下，川久保玲、 Miu 都是这个经典的版型，而且增加了一些小设计。肩线都是这种正边的版型，每个颜色都好好看，特别是这个铁锈红！过年回家给自己带一件，妈妈带一件！再不入手就来不及啦！\",\"Template_Class\":\"S&W 营销\"},{\"ID\":10,\"Template\":\"就这个版型，你穿 5 年、 10 年都不会过时，很经典！很有品位！如果纠结颜色的，直接去冲灰色！肩线都是这种正边的版型，不是收腰的，它偏慵懒，上身就是一个三七分，搭休闲裤、牛仔裤、长裙、短裙。真的很百搭啊，姐妹们！\",\"Template_Class\":\"S&W 营销\"}]}"
  }


function main({result}){
    const resultJson = JSON.parse(result)
    const hhh = resultJson.result

    // 拿到目标信息
    const clearList = []
    const templateList = []
    hhh.forEach(item =>{
        const  {Template_Class, ...temp} = item
        clearList.push(temp)
        templateList.push(temp.Template)
    })

    return {
        template_info:clearList,
        template: templateList

    }

}


let hhh = main(data)
console.log(hhh.template_info)
