import os
import datetime
import yagmail

SENDER_EMAIL = os.environ['SENDER_EMAIL']
SENDER_PASS = os.environ['SENDER_PASS']
RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']

def get_news():
    # TODO: Replace this list with your news fetching logic
    # For now, manually maintain the news list
    return [
        "OpenAI 推出 GPT-5，能力提升显著。",
        "微软集成 Copilot 于 Azure 全线产品。",
        "Google Gemini 2.0 支持100多种语言和代码自动修正。",
        "Anthropic 训练出更安全的Claude智能体。",
        "Meta 发布开源AGI框架。",
        "阿里云灵越推出可商用AI Agent服务。",
        "NVIDIA 发布智能体开发专用GPU及SDK。",
        "百度文心Agent支持企业级知识库管理。",
        "Hugging Face上线智能体模型榜单与Benchmark。",
        "特斯拉公开Robotaxi智能体控制算法。",
        "腾讯混元Agent可对接CRM与OA系统。",
        "DeepMind发布通用强化学习智能体X。",
        "Notion集成AI助手自动生成会议纪要与任务清单。",
        "亚马逊Alexa大升级，面向家庭RPA和IoT场景。",
        "Stability AI发布可控文本驱动3D Agent。",
        "Salesforce Einstein Agent能自动处理客户请求。",
        "小米汽车搭载全新驾驶AI及车辆虚拟助手。",
        "Replit 支持直接用智能体修复和优化代码。",
        "AI Agent伦理和监管议题升温，欧盟新规正式生效。",
        "清华团队夺AI Agent竞赛全球第一。",
    ]

def format_news(news_list):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    content = f"AI智能体领域重要新闻摘要（{today}）\n\n"
    content += '\n'.join([f"{i+1}. {n}" for i, n in enumerate(news_list)])
    return content

def send_email(subject, content):
    # Initialize SMTP
    yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASS, host='smtp.163.com')
    yag.send(
        to=RECEIVER_EMAIL,
        subject=subject,
        contents=content
    )
    print('邮件发送成功！')

if __name__ == '__main__':
    news = get_news()
    content = format_news(news)
    send_email(f'AI智能体新闻摘要 {datetime.datetime.now().strftime("%Y-%m-%d")}', content)
