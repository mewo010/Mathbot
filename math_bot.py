import datetime
import os
import random
import requests

# ---------- Environment Variables ----------
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
# Can be a single chat ID (e.g., "-123456789") or multiple separated by commas.
TELEGRAM_CHAT_IDS = os.environ.get("TELEGRAM_CHAT_ID", "")

# ---------- Data ----------
scientific_math_curriculum = [
    {
        "day": 1,
        "category": "פונקציה קווית",
        "topic": "הכרת הפונקציה הקווית, שיפוע ונקודת חיתוך עם הצירים",
        "video_title": "פונקציה קווית - שיפוע ומשוואת ישר",
        "video_url": "http://www.youtube.com/watch?v=oNL8UeweimY",
    },
    {
        "day": 2,
        "category": "פונקציה קווית",
        "topic": "מציאת משוואת ישר על פי נקודה ושיפוע או שתי נקודות",
        "video_title": "מציאת משוואת ישר - מתמטיקה כיתה ח",
        "video_url": "http://www.youtube.com/watch?v=Omq2QIl4u0w",
    },
    {
        "day": 3,
        "category": "פונקציה קווית",
        "topic": "ישרים מקבילים וישרים ניצבים במערכת הצירים",
        "video_title": "ישרים מקבילים וניצבים פונקציה קווית",
        "video_url": "http://www.youtube.com/watch?v=c1TyO6wqwmY",
    },
    {
        "day": 4,
        "category": "מערכת משוואות",
        "topic": "פתרון מערכת משוואות קוויות בשיטת ההצבה וההשוואה",
        "video_title": "מערכת משוואות קוויות - שיטת ההצבה",
        "video_url": "http://www.youtube.com/watch?v=EV6i96qpVlY",
    },
    {
        "day": 5,
        "category": "מערכת משוואות",
        "topic": "פתרון מערכת משוואות בשיטת השוואת מדדים / חיבור וחיסור",
        "video_title": "מערכת משוואות שיטת החיסור והחיבור",
        "video_url": "http://www.youtube.com/watch?v=oNL8UeweimY",
    },
    {
        "day": 6,
        "category": "משוואות ואי שוויונות",
        "topic": "משוואות עם נעלם אחד המכילות שברים ואלגברה מתקדמת",
        "video_title": "משוואות עם שברים - אלגברה כיתה ח",
        "video_url": "http://www.youtube.com/watch?v=c1TyO6wqwmY",
    },
    {
        "day": 7,
        "category": "משוואות ואי שוויונות",
        "topic": "אי שוויונות ליניאריים עם נעלם אחד וייצוג פתרון על ציר המספרים",
        "video_title": "אי שוויונות כיתה ח - הסבר ותרגול",
        "video_url": "http://www.youtube.com/watch?v=c1TyO6wqwmY",
    },
    {
        "day": 8,
        "category": "שברים אלגבריים",
        "topic": "צמצום שברים אלגבריים והוצאת גורם משותף",
        "video_title": "שברים אלגבריים צמצום ופירוק לגורמים",
        "video_url": "http://www.youtube.com/watch?v=Omq2QIl4u0w",
    },
    {
        "day": 9,
        "category": "שברים אלגבריים",
        "topic": "חיבור וחיסור של שברים אלגבריים עם מכנה משודרג",
        "video_title": "חיבור וחיסור שברים אלגבריים מתמטיקה",
        "video_url": "http://www.youtube.com/watch?v=EV6i96qpVlY",
    },
    {
        "day": 10,
        "category": "סטטיסטיקה ואחוזים",
        "topic": "בעיות אחוזים מתקדמות (הנחות, רווח והפסד, שיעור השינוי)",
        "video_title": "בעיות אחוזים מתמטיקה כיתה ח",
        "video_url": "http://www.youtube.com/watch?v=c1TyO6wqwmY",
    },
    {
        "day": 11,
        "category": "סטטיסטיקה ואחוזים",
        "topic": "ממוצע משוקלל, חציון ושכיח בסטטיסטיקה מתקדמת",
        "video_title": "סטטיסטיקה ממוצע שכיח חציון כיתה ח",
        "video_url": "http://www.youtube.com/watch?v=oNL8UeweimY",
    },
    {
        "day": 12,
        "category": "אוריינות ושאלות מילוליות",
        "topic": "בעיות תנועה (הספק, דרך, מהירות, זמנים בשילוב משוואות)",
        "video_title": "בעיות תנועה והספק - הכנה למגמה מדעית",
        "video_url": "http://www.youtube.com/watch?v=EV6i96qpVlY",
    },
    {
        "day": 13,
        "category": "אוריינות ושאלות מילוליות",
        "topic": "בעיות קנייה ומכירה והנחות באחוזים",
        "video_title": "בעיות מילוליות אחוזים כיתה ח",
        "video_url": "http://www.youtube.com/watch?v=Omq2QIl4u0w",
    },
    {
        "day": 14,
        "category": "גיאומטריה במערכת צירים",
        "topic": "חישוב אורכי קטעים אנכיים ואופקיים במערכת הצירים",
        "video_title": "גיאומטריה אנליטית מרחק בין נקודות",
        "video_url": "http://www.youtube.com/watch?v=c1TyO6wqwmY",
    },
    {
        "day": 15,
        "category": "גיאומטריה במערכת צירים",
        "topic": "חישוב שטחי משולשים ומרובעים הממוקמים במערכת הצירים",
        "video_title": "שטח משולש במערכת צירים גיאומטריה אנליטית",
        "video_url": "http://www.youtube.com/watch?v=EV6i96qpVlY",
    },
    {
        "day": 16,
        "category": "חוקי חזקות",
        "topic": "חוקי חזקות עם בסיסים שליליים ומעריכים אלגבריים",
        "video_title": "חוקי חזקות - המדריך המלא",
        "video_url": "http://www.youtube.com/watch?v=c1TyO6wqwmY",
    },
    {
        "day": 17,
        "category": "כפל מקוצר",
        "topic": "נוסחאות הכפל המקוצר הראשונה והשנייה ($a+b)^2$",
        "video_title": "נוסחאות הכפל המקוצר הסבר מלא",
        "video_url": "http://www.youtube.com/watch?v=Omq2QIl4u0w",
    },
    {
        "day": 18,
        "category": "כפל מקוצר",
        "topic": "נוסחת הפרש הריבועים ופירוק מתקדם לגורמים",
        "video_title": "הפרש הריבועים פירוק לגורמים כיתה ט",
        "video_url": "http://www.youtube.com/watch?v=EV6i96qpVlY",
    },
    {
        "day": 19,
        "category": "חזרה מקיפה",
        "topic": "שילוב משוואות ופונקציה קווית - שאלות ברמת מבחן מעבר",
        "video_title": "חזרה למבחן מעבר למגמה מדעית מתמטיקה",
        "video_url": "http://www.youtube.com/watch?v=oNL8UeweimY",
    },
    {
        "day": 20,
        "category": "אתגר מסכם",
        "topic": "שאלות אוריינות קשות ואתגרי חשיבה אלגבריים",
        "video_title": "אתגר חשיבה מתמטיקה כיתה ח ט",
        "video_url": "http://www.youtube.com/watch?v=c1TyO6wqwmY",
    },
]

motivation_quotes = [
    {"quote": "הדרך הטובה ביותר לחזות את העתיד היא ליצור אותו.", "author": "פטר דרוקר"},
    {"quote": "לעולם אל תפסיק ללמוד, כי החיים מעולם לא מפסיקים ללמד.", "author": "אנונימי"},
    {"quote": "ההצלחה אינה סופית, הכישלון אינו קטלני: האומץ להמשיך הוא שקובע.", "author": "ווינסטון צ'רצ'יל"},
    {"quote": "תאמין שאתה יכול, ואתה כבר חצי הדרך שם.", "author": "תיאדור רוזוולט"},
    {"quote": "למדו אתמול, חיו היום, תקוו למחר. הדבר החשוב ביותר הוא לא להפסיק לשאול שאלות.", "author": "אלברט איינשטיין"},
    {"quote": "הקשיים נועדו להכניע אותנו או לחשל אותנו. הבחירה בידיים שלנו.", "author": "אריסטו"},
    {"quote": "עתידך תלוי במה שאתה עושה היום, לא מחר.", "author": "מהטמה גנדי"},
    {"quote": "אל תפחד ללכת לאט, תפחד רק לעמוד במקום.", "author": "פתגם סיני"},
    {"quote": "הדרך לידע רצופה בשאלות קשות ובסקרנות בלתי פוסקת.", "author": "אייזק ניוטון"},
    {"quote": "כל מומחה גדול היה פעם מתחיל גמור שלא ויתר.", "author": "הלן קלר"},
]

# ---------- Core Function ----------
def send_telegram_task():
    if not TELEGRAM_BOT_TOKEN:
        print("❌ שגיאה: TELEGRAM_BOT_TOKEN לא הוגדר.")
        return

    # Parse chat IDs (support comma-separated list, trim whitespace)
    chat_ids = [cid.strip() for cid in TELEGRAM_CHAT_IDS.split(",") if cid.strip()]
    if not chat_ids:
        print("❌ שגיאה: TELEGRAM_CHAT_ID לא הוגדר.")
        return

    # Build the message (same as before)
    day_index = (datetime.datetime.now().day - 1) % len(scientific_math_curriculum)
    task = scientific_math_curriculum[day_index]
    random_quote = random.choice(motivation_quotes)

    message = (
        f"🌟 *מוטיבציה להיום:*\n"
        f"💬 *\"{random_quote['quote']}\"*\n"
        f"— {random_quote['author']}\n\n"
        f"-----------------------------------\n\n"
        f"🎯 *אימון יומי בחשבון - מגמה מדעית (כיתה ט)* 🎯\n\n"
        f"📂 *קטגוריה:* {task['category']}\n"
        f"📌 *נושא להיום:* {task['topic']}\n\n"
        f"📺 *סרטון לצפייה:* \n"
        f"[{task['video_title']}]({task['video_url']})\n\n"
        f"💡 *משימה להיום:* צפה בסרטון בעיון, רשום את הדגשים במחברת, ופתור לפחות 3-4 תרגילים מתקדמים ברמת קושי גבוהה.\n\n"
        f"בהצלחה! המשך קיץ פרודוקטיבי 💪"
    )

    # Send to each chat ID
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload_base = {
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False,
    }

    success_count = 0
    for chat_id in chat_ids:
        payload = payload_base.copy()
        payload["chat_id"] = chat_id
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ הודעה נשלחה בהצלחה ל־{chat_id}")
                success_count += 1
            else:
                print(f"❌ שגיאה בשליחה ל־{chat_id}: {response.text}")
        except Exception as e:
            print(f"❌ שגיאה בשליחה ל־{chat_id}: {e}")

    if success_count == len(chat_ids):
        print("🎉 כל ההודעות נשלחו בהצלחה!")
    else:
        print(f"⚠️ נשלחו {success_count} מתוך {len(chat_ids)} הודעות.")

if __name__ == "__main__":
    send_telegram_task()
