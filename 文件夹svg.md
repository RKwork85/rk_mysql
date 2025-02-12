

function main({data1}){

    // 正则表达式匹配代码块中的内容
    const codeBlockRegex = /```[\w]*\n([\s\S]*?)```/;
    const codeMatch = data1.match(codeBlockRegex);

    // 正则表达式匹配 <thinking></thinking> 标签中的内容
    const thinkingRegex = /<thinking>([\s\S]*?)<\/thinking>/;
    const thinkingMatch = data1.match(thinkingRegex);


    // 处理代码块内容
    let base64 = null;
    if (codeMatch) {
        const extractedSvg = codeMatch[1].trim();
        base64 = strToBase64(extractedSvg, 'data:image/svg+xml;base64,');
    } else {
        // 如果没有找到代码块，返回错误信息
        return {
            result: null,
            thinking: null,
            error: "未找到有效的代码块标记。"
        };
    }


    return {
        result: base64,
    }
}


模板
`
<svg width="600" height="800" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .folder { font-size: 14px; fill: #333; }
      .line { stroke: #ccc; stroke-width: 1; }
      .icon { fill: #ffcc00; }
    </style>
  </defs>

  <!-- 树形目录的根节点 -->
  <g transform="translate(50, 50)">
    <!-- 根文件夹 -->
    <g transform="translate(0, 0)">
      <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
      <text class="folder" x="25" y="15" id="root-folder">根文件夹</text>
      <line class="line" x1="10" y1="30" x2="10" y2="50" />
      <line class="line" x1="10" y1="50" x2="30" y2="50" />
    </g>

    <!-- 子文件夹 1 -->
    <g transform="translate(20, 50)">
      <g transform="translate(0, 0)">
        <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
        <text class="folder" x="25" y="15" id="sub-folder-1">子文件夹 1</text>
        <line class="line" x1="10" y1="30" x2="10" y2="50" />
        <line class="line" x1="10" y1="50" x2="30" y2="50" />
      </g>

      <!-- 子文件夹 1-1 -->
      <g transform="translate(20, 50)">
        <g transform="translate(0, 0)">
          <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
          <text class="folder" x="25" y="15" id="sub-folder-1-1">子文件夹 1-1</text>
          <line class="line" x1="10" y1="30" x2="10" y2="50" />
          <line class="line" x1="10" y1="50" x2="30" y2="50" />
        </g>
      </g>

      <!-- 子文件夹 1-2 -->
      <g transform="translate(20, 100)">
        <g transform="translate(0, 0)">
          <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
          <text class="folder" x="25" y="15" id="sub-folder-1-2">子文件夹 1-2</text>
          <line class="line" x1="10" y1="30" x2="10" y2="50" />
          <line class="line" x1="10" y1="50" x2="30" y2="50" />
        </g>
      </g>
    </g>

    <!-- 子文件夹 2 -->
    <g transform="translate(20, 200)">
      <g transform="translate(0, 0)">
        <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
        <text class="folder" x="25" y="15" id="sub-folder-2">子文件夹 2</text>
        <line class="line" x1="10" y1="30" x2="10" y2="50" />
        <line class="line" x1="10" y1="50" x2="30" y2="50" />
      </g>
    </g>
  </g>
</svg>
`


&lt;svg width="600" height="800" xmlns="http://www.w3.org/2000/svg"&gt;
  &lt;defs&gt;
    &lt;style&gt;
     .folder { font-size: 14px; fill: #333; }
     .line { stroke: #ccc; stroke-width: 1; }
     .icon { fill: #ffcc00; }
    &lt;/style&gt;
  &lt;/defs&gt;

  &lt;!-- 树形目录的根节点 --&gt;
  &lt;g transform="translate(50, 50)"&gt;
    &lt;!-- 根文件夹 --&gt;
    &lt;g transform="translate(0, 0)"&gt;
      &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
      &lt;text class="folder" x="25" y="15" id="root-folder"&gt;"S&amp;W_S2AW1423"&lt;/text&gt;
      &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
      &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
    &lt;/g&gt;

    &lt;!-- 子文件夹 岩雾灰/岩雾白/深邃黑/月牙白/稻田黄/橄榄绿/岩雾紫/黑迷彩 --&gt;
    &lt;g transform="translate(20, 50)"&gt;
      &lt;g transform="translate(0, 0)"&gt;
        &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
        &lt;text class="folder" x="25" y="15" id="sub-folder-1"&gt;岩雾灰/岩雾白/深邃黑/月牙白/稻田黄/橄榄绿/岩雾紫/黑迷彩&lt;/text&gt;
        &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
        &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
      &lt;/g&gt;

      &lt;!-- 子文件夹 整体画面 --&gt;
      &lt;g transform="translate(20, 50)"&gt;
        &lt;g transform="translate(0, 0)"&gt;
          &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
          &lt;text class="folder" x="25" y="15" id="sub-folder-2"&gt;整体画面&lt;/text&gt;
          &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
          &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
        &lt;/g&gt;

        &lt;!-- 子文件夹 模特展示 --&gt;
        &lt;g transform="translate(20, 50)"&gt;
          &lt;g transform="translate(0, 0)"&gt;
            &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
            &lt;text class="folder" x="25" y="15" id="sub-folder-3"&gt;模特展示&lt;/text&gt;
            &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
            &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
          &lt;/g&gt;

          &lt;!-- 子文件夹 静态展示 --&gt;
          &lt;g transform="translate(20, 50)"&gt;
            &lt;g transform="translate(0, 0)"&gt;
              &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
              &lt;text class="folder" x="25" y="15" id="sub-folder-4"&gt;静态展示&lt;/text&gt;
              &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
              &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
            &lt;/g&gt;
          &lt;/g&gt;

          &lt;!-- 子文件夹 动态展示 --&gt;
          &lt;g transform="translate(20, 100)"&gt;
            &lt;g transform="translate(0, 0)"&gt;
              &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
              &lt;text class="folder" x="25" y="15" id="sub-folder-5"&gt;动态展示&lt;/text&gt;
              &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
              &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
            &lt;/g&gt;
          &lt;/g&gt;
        &lt;/g&gt;

        &lt;!-- 子文件夹 产品展示 --&gt;
        &lt;g transform="translate(20, 100)"&gt;
          &lt;g transform="translate(0, 0)"&gt;
            &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
            &lt;text class="folder" x="25" y="15" id="sub-folder-6"&gt;产品展示&lt;/text&gt;
            &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
            &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
          &lt;/g&gt;

          &lt;!-- 子文件夹 悬挂展示 --&gt;
          &lt;g transform="translate(20, 50)"&gt;
            &lt;g transform="translate(0, 0)"&gt;
              &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
              &lt;text class="folder" x="25" y="15" id="sub-folder-7"&gt;悬挂展示&lt;/text&gt;
              &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
              &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
            &lt;/g&gt;
          &lt;/g&gt;

          &lt;!-- 子文件夹 平铺展示 --&gt;
          &lt;g transform="translate(20, 100)"&gt;
            &lt;g transform="translate(0, 0)"&gt;
              &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
              &lt;text class="folder" x="25" y="15" id="sub-folder-8"&gt;平铺展示&lt;/text&gt;
              &lt;line class="line" x1="10" y1="30" x2="10" y2="50" /&gt;
              &lt;line class="line" x1="10" y1="50" x2="30" y2="50" /&gt;
            &lt;/g&gt;
          &lt;/g&gt;

          &lt;!-- 子文件夹 对比展示 --&gt;
          &lt;g transform="translate(20, 150)"&gt;
            &lt;g transform="translate(0, 0)"&gt;
              &lt;path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" /&gt;
              &lt;text class="folder" x="25" y="15" id="sub-folder-9"&gt;对比展示&lt;/text&gt;
              &lt;line class="line" x1="10" y1="30" x




<svg width="600" height="800" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
     .folder { font-size: 14px; fill: #333; }
     .line { stroke: #ccc; stroke-width: 1; }
     .icon { fill: #ffcc00; }
    </style>
  </defs>

  <!-- 树形目录的根节点 -->
  <g transform="translate(50, 50)">
    <!-- 根文件夹 -->
    <g transform="translate(0, 0)">
      <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
      <text class="folder" x="25" y="15" id="root-folder">S&W_S2AW1423</text>
      <line class="line" x1="10" y1="30" x2="10" y2="50" />
      <line class="line" x1="10" y1="50" x2="30" y2="50" />
    </g>

    <!-- 子文件夹 岩雾灰/岩雾白/深邃黑/月牙白/稻田黄/橄榄绿/岩雾紫/黑迷彩 -->
    <g transform="translate(20, 50)">
      <g transform="translate(0, 0)">
        <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
        <text class="folder" x="25" y="15" id="sub-folder-1">岩雾灰/岩雾白/深邃黑/月牙白/稻田黄/橄榄绿/岩雾紫/黑迷彩</text>
        <line class="line" x1="10" y1="30" x2="10" y2="50" />
        <line class="line" x1="10" y1="50" x2="30" y2="50" />
      </g>

      <!-- 子文件夹 整体画面 -->
      <g transform="translate(20, 50)">
        <g transform="translate(0, 0)">
          <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
          <text class="folder" x="25" y="15" id="sub-folder-2">整体画面</text>
          <line class="line" x1="10" y1="30" x2="10" y2="50" />
          <line class="line" x1="10" y1="50" x2="30" y2="50" />
        </g>

        <!-- 子文件夹 模特展示 -->
        <g transform="translate(20, 50)">
          <g transform="translate(0, 0)">
            <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
            <text class="folder" x="25" y="15" id="sub-folder-3">模特展示</text>
            <line class="line" x1="10" y1="30" x2="10" y2="50" />
            <line class="line" x1="10" y1="50" x2="30" y2="50" />
          </g>

          <!-- 子文件夹 静态展示 -->
          <g transform="translate(20, 50)">
            <g transform="translate(0, 0)">
              <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
              <text class="folder" x="25" y="15" id="sub-folder-4">静态展示</text>
              <line class="line" x1="10" y1="30" x2="10" y2="50" />
              <line class="line" x1="10" y1="50" x2="30" y2="50" />
            </g>
          </g>

          <!-- 子文件夹 动态展示 -->
          <g transform="translate(20, 100)">
            <g transform="translate(0, 0)">
              <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
              <text class="folder" x="25" y="15" id="sub-folder-5">动态展示</text>
              <line class="line" x1="10" y1="30" x2="10" y2="50" />
              <line class="line" x1="10" y1="50" x2="30" y2="50" />
            </g>
          </g>
        </g>

        <!-- 子文件夹 产品展示 -->
        <g transform="translate(20, 100)">
          <g transform="translate(0, 0)">
            <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
            <text class="folder" x="25" y="15" id="sub-folder-6">产品展示</text>
            <line class="line" x1="10" y1="30" x2="10" y2="50" />
            <line class="line" x1="10" y1="50" x2="30" y2="50" />
          </g>

          <!-- 子文件夹 悬挂展示 -->
          <g transform="translate(20, 50)">
            <g transform="translate(0, 0)">
              <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
              <text class="folder" x="25" y="15" id="sub-folder-7">悬挂展示</text>
              <line class="line" x1="10" y1="30" x2="10" y2="50" />
              <line class="line" x1="10" y1="50" x2="30" y2="50" />
            </g>
          </g>

          <!-- 子文件夹 平铺展示 -->
          <g transform="translate(20, 100)">
            <g transform="translate(0, 0)">
              <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
              <text class="folder" x="25" y="15" id="sub-folder-8">平铺展示</text>
              <line class="line" x1="10" y1="30" x2="10" y2="50" />
              <line class="line" x1="10" y1="50" x2="30" y2="50" />
            </g>
          </g>

          <!-- 子文件夹 对比展示 -->
          <g transform="translate(20, 150)">
            <g transform="translate(0, 0)">
              <path class="icon" d="M5 0 L15 0 L20 5 L20 20 L0 20 L0 5 L5 5 Z" />
              <text class="folder" x="25" y="15" id="sub-folder-9">对比展示</text>
              <line class="line" x1="10" y1="30" x