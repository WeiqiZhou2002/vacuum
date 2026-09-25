# Vacuum Shortcut

Universal Shortcut 的名称为 `Vacuum`，通过[官方 iCloud 链接](https://www.icloud.com/shortcuts/79c33516e80441dda719c907c2b5dcf3)安装。repository 不保存 Shortcut binary。

安装时，在 Import Question 中选择：

```text
Vacuum → 00 收件箱
```

## 最终行为

支持系统分享的 App：

```text
分享 → Vacuum
```

小红书：

```text
复制链接 → Vacuum
```

可选 Back Tap：

```text
Back Tap → Vacuum
```

Shortcut 优先使用 Share Sheet Input；没有 Share Sheet Input 时使用 Clipboard。随后询问「为什么值得收藏？」，并把一条 timestamped Markdown Capture 写入 `00 收件箱`。

## Import Question

问题文字：

> 请选择 Vacuum 的「00 收件箱」文件夹

参考路径：

> iCloud Drive → Obsidian → Vacuum → 00 收件箱

Import Question 的真实绑定行为仍需在实际 iPhone 上验证。不要把 URL 或 捕获内容 描述为已经归档的原帖。

## 仍需真实设备验证

- 小红书复制链接；
- Bilibili、Safari 与其他兼容 App 的 Share Sheet payload；
- Clipboard fallback；
- 同秒 filename collision；
- Import Question 与目标文件夹绑定；
- iCloud cross-device sync timing 与 Mac 文件可见性；
- 新设备安装。
