# 📢 Voice Meeting Recording Announcements

---

## **1️⃣ General Members Announcement**

**📢 Notice: Voice Meetings May Be Recorded for Reference**

Hello everyone! 👋  

To help moderators **capture questions, proposals, and discussion points accurately**, voice meetings **may now be recorded by authorized moderators**.  

**How it works:**  
- Only approved moderators can start a recording.  
- When a recording starts, a **notice will appear in the text channel**, and all participants will receive a DM informing them the session is being recorded.  
- If you join while a recording is in progress, you’ll also be notified.  
- Recordings are kept **private and secure**, and are only used for internal reference to ensure no points or questions are missed.  

**Your participation:**  
- By staying in a recorded meeting, you **consent** to being recorded.  
- If you prefer not to be recorded, you may **leave the session** or **contact moderators** to request deletion of your participation from the recording.  

We are implementing this to make meetings more productive and ensure **every voice is heard**. Thank you for your understanding!  

— *The Moderation Team*

---

## **2️⃣ Staff / Moderator Announcement**

**📌 Staff Guide: Using the Craig Recording Notification Bot**

Hello moderators! 🛡️  

We’ve implemented a system to record voice meetings while keeping members informed. Here’s everything you need to know:

### **How the system works**
1. **Starting a Recording:**  
   - Only authorized moderators can summon Craig to start recording a voice channel.  
   - When Craig joins, the **Notification Bot** will automatically:  
     - Send a **DM to all connected users** informing them of the recording.  
     - Post a **log message in the designated text channel** for auditing.  

2. **During the Recording:**  
   - The bot monitors all voice channel joins.  
   - **New members** who enter while recording is active will receive a DM notification automatically.  
   - The bot ensures **no repeated notifications** are sent to the same user for the same session.  

3. **Ending a Recording:**  
   - When Craig leaves, the bot logs the session end and can optionally post a **final notice** in the text channel.  
   - Users who want access or deletion can contact staff for requests.  
   - Internal logs provide **an audit trail** for compliance and transparency.  

### **Important Staff Notes**
- Only summon Craig when necessary — recordings are **for reference only**, not for public sharing.  
- Always check that all participants are notified; the bot handles this automatically, but verify DMs if needed.  
- Store recordings securely and limit access to **authorized staff only**.  
- Make sure the **Notification Bot is online** and has proper permissions (Send Messages, Read Message History, View Channels).  

### **Permissions & Setup**
- The bot requires:  
  - `SERVER MEMBERS INTENT`, `PRESENCE INTENT`, `MESSAGE CONTENT INTENT` enabled  
  - Proper OAuth2 permissions: View Channels, Send Messages, Read Message History, Mention Everyone (if needed)  
- Logs are stored in the configured text channel for auditing.  

**Goal:**  
Ensure meetings are **accurately captured** without missing questions or proposals, while maintaining **full transparency and privacy** for all participants.
