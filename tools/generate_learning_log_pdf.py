from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle


ROOT = Path(r"C:\Users\HUAWEI\Documents\codex-restart")
PDF_PATH = ROOT / "output" / "pdf" / "codex-learning-log-2026-06-29.pdf"
FONT_PATH = r"C:\Windows\Fonts\simhei.ttf"


def make_styles():
    pdfmetrics.registerFont(TTFont("SimHei", FONT_PATH))
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCN",
            fontName="SimHei",
            fontSize=24,
            leading=32,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#111827"),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubCN",
            fontName="SimHei",
            fontSize=10.5,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4b5563"),
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2CN",
            fontName="SimHei",
            fontSize=15,
            leading=22,
            textColor=colors.HexColor("#111827"),
            spaceBefore=10,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCN",
            fontName="SimHei",
            fontSize=10.5,
            leading=17,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallCN",
            fontName="SimHei",
            fontSize=9,
            leading=14,
            textColor=colors.HexColor("#374151"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeCN",
            fontName="SimHei",
            fontSize=9.5,
            leading=15,
            textColor=colors.HexColor("#111827"),
            backColor=colors.HexColor("#f3f4f6"),
            leftIndent=8,
            rightIndent=8,
            spaceBefore=4,
            spaceAfter=8,
        )
    )
    return styles


def build_pdf():
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    story = []

    def p(text, style="BodyCN"):
        story.append(Paragraph(text, styles[style]))

    def h(text):
        story.append(Paragraph(text, styles["H2CN"]))

    def code(text):
        story.append(Paragraph(text.replace("\n", "<br/>"), styles["CodeCN"]))

    def cell(text):
        return Paragraph(text, styles["SmallCN"])

    story.append(Paragraph("Codex 入门学习记录", styles["TitleCN"]))
    story.append(
        Paragraph(
            "日期：2026-06-29  |  项目：codex-restart  |  学习者：王维",
            styles["SubCN"],
        )
    )
    p(
        "这份 PDF 整理了今天的 Codex 入门学习对话和实践过程：从创建第一个网页，"
        "到使用 VS Code、Git、GitHub，再到通过 GitHub Pages 发布成可访问网址。"
    )
    p("最终网页地址： https://why911-1.github.io/codex-restart/codex-practice/")

    h("一、今天完成的主要结果")
    rows = [
        ["阶段", "学习内容", "结果"],
        ["Codex 入门", "理解 Codex 的基本工作流：查看环境、修改文件、读回确认。", "建立了练习项目。"],
        ["网页制作", "创建自我介绍网页，并拆分为 HTML、CSS、JavaScript 三个文件。", "本地可预览。"],
        ["VS Code", "学会打开项目文件夹，查看左侧文件列表，并手动修改 HTML。", "建立“修改-保存-刷新”循环。"],
        ["Git", "初始化仓库，完成第一次提交，又完成一次修改后提交。", "本地有版本记录。"],
        ["GitHub", "发布到 GitHub 仓库，学会识别小锁图标表示 Private。", "代码上传成功。"],
        ["GitHub Pages", "开启 Pages，理解私有仓库的 Pages 限制。", "网页成功上线。"],
    ]
    table = Table([[cell(c) for c in row] for row in rows], colWidths=[30 * mm, 94 * mm, 44 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e5e7eb")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d1d5db")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(table)

    h("二、对话和练习记录")
    items = [
        ("入门引导", "你说自己是 Codex 新手，希望我做入门引导。我们采用“边学边做”的方式。"),
        ("练习1：认识工作区", "检查当前文件夹，发现它原本基本为空，并且还不是 Git 项目。我创建了 codex-practice/hello.md 作为练习起点。"),
        ("练习2：中文自我介绍模板", "你把模板填成了王维、昆明、员工、正在学习 Codex。"),
        ("练习3：创建网页", "根据自我介绍创建 codex-practice/index.html，包含头像、基本信息、自我介绍和学习目标。"),
        ("练习4：添加互动", "添加“显示欢迎语”按钮，点击后显示欢迎你的文字。"),
        ("练习5：解释代码", "总结为：HTML 放内容，CSS 管好看，JavaScript 管互动。"),
        ("练习6：VS Code", "解释了浏览器、VS Code、Codex 的分工，并带你打开项目文件夹。"),
        ("练习7：拆分文件", "把 index.html 中的 CSS 和 JavaScript 分离到 style.css 和 script.js。你后来手动把按钮文字改成“点我看看”。"),
        ("Git 和 GitHub", "你在 VS Code 里初始化仓库，填写提交信息，完成第一次提交，并发布到 GitHub：https://github.com/why911-1/codex-restart。"),
        ("练习9：再次提交并同步", "修改页脚为“Codex Practice - 练习 9：再次提交并同步”，经历一次 GitHub 网络连接失败后，最终同步成功。"),
        ("练习10：GitHub Pages", "学习如何把 GitHub 上的网页变成网址。页面最终通过 GitHub Pages 发布成功。"),
    ]
    for title, body in items:
        p(f"<b>{title}</b>：{body}")

    h("三、项目文件结构")
    code("codex-restart\n  codex-practice\n    hello.md\n    index.html\n    style.css\n    script.js")
    p(
        "index.html 负责网页结构，style.css 负责颜色、布局和样式，"
        "script.js 负责点击按钮后的互动逻辑。"
    )

    h("四、重要概念速记")
    concepts = [
        ["概念", "意思"],
        ["浏览器", "用来查看网页效果。"],
        ["VS Code", "用来查看和编辑代码。"],
        ["Codex", "帮助你理解、修改、检查和生成项目内容。"],
        ["Git", "本地版本管理工具。"],
        ["GitHub", "云端代码仓库网站。"],
        ["commit", "保存一个版本。"],
        ["push / sync", "把本地提交上传到 GitHub。"],
        ["Private", "私有仓库，代码默认只有你能看。"],
        ["GitHub Pages", "把静态网页发布成网址。"],
    ]
    table2 = Table([[cell(c) for c in row] for row in concepts], colWidths=[42 * mm, 126 * mm])
    table2.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e5e7eb")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d1d5db")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(table2)

    h("五、以后修改项目的标准流程")
    code(
        "1. 在 VS Code 修改文件\n"
        "2. Ctrl + S 保存\n"
        "3. 在浏览器刷新查看效果\n"
        "4. 打开源代码管理\n"
        "5. 输入提交说明\n"
        "6. 点击提交\n"
        "7. 点击同步更改\n"
        "8. 刷新 GitHub 或 GitHub Pages 确认结果"
    )

    h("六、今天遇到的问题")
    p("中文终端显示乱码：这是 Windows 终端编码问题，后来通过 UTF-8 读取确认内容正常。")
    p("COMMIT_EDITMSG 页面：这是 Git 让你填写提交说明的文件，要写在第一行，不要写在 # 开头的注释行。")
    p("GitHub 网络失败：出现无法连接 github.com:443 时，本地提交不会丢，网络恢复后再点同步即可。")
    p("GitHub Pages 私有仓库限制：私有仓库要启用 Pages 通常需要升级或改为公开。")

    h("七、明天建议继续学习")
    p(
        "建议从练习11开始：给网页增加一个输入框，让用户输入名字后生成欢迎语。"
        "这会继续练习 HTML 表单、JavaScript 读取输入、页面更新，以及再次提交同步的完整流程。"
    )

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("SimHei", 8)
        canvas.setFillColor(colors.HexColor("#6b7280"))
        canvas.drawString(18 * mm, 12 * mm, "Codex 入门学习记录")
        canvas.drawRightString(195 * mm, 12 * mm, f"第 {doc.page} 页")
        canvas.restoreState()

    pdf = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=20 * mm,
    )
    pdf.build(story, onFirstPage=footer, onLaterPages=footer)
    print(PDF_PATH)


if __name__ == "__main__":
    build_pdf()
