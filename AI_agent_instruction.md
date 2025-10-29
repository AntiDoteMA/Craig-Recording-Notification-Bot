# AI Agent Instructions: Craig Recording Notification Bot

## Objective
Build an AI-powered Discord bot that works alongside Craig Bot to ensure ethical voice recording by:

1. Detecting when Craig starts or stops recording in a voice channel.
2. Automatically notifying all current voice channel members via DM that the channel is being recorded.
3. Automatically notifying any new users who join the channel during recording.
4. Providing instructions for users to request removal of their recording within a 24-hour window.
5. Optionally logging notifications in a designated text channel.
6. Integrating with a ticketing system for removal requests.

---

## Functional Requirements

### 1. Detection
- Monitor **voice_state_update** events on the Discord server.
- Detect when a bot with `"craig"` in its username joins or leaves a voice channel.
- Keep a **list of active recording channels** to track ongoing recordings.

### 2. Notifications
- For all users currently in the channel:
  - Send a **direct message (DM)**:
    ```
    ⚠️ Notice: The voice channel {channel_name} is currently being recorded by Craig Bot.
    If you do not consent, please leave immediately.
    If you wish your recording removed, open a ticket within 24 hours at #support.
    ```
  - Skip sending DMs to bots.
- For **new users who join** a channel while recording:
  - Automatically DM them with the same message.

### 3. Logging
- Optionally send a **log message** in a text channel (`#recording-log`) for each notification:
[TIMESTAMP] User {user_name} notified about recording in {channel_name}.

yaml
Copy code
- Log when Craig joins or leaves a voice channel.

### 4. Ticket System Integration
- Include a **link or instruction** in the DM to open a ticket for removal requests.
- Ensure the ticket is **timestamped** for tracking the 24-hour consent window.
- Optionally automate ticket creation using a compatible support bot.

### 5. Edge Cases
- If a user disconnects and reconnects: resend the notification only once per session.
- Stop monitoring a channel when Craig leaves.
- Respect Discord DM restrictions (catch `discord.Forbidden` exceptions).

---

## Non-Functional Requirements
- Written in **Python** using `discord.py` or equivalent library.
- Maintain **high reliability**: track active recording channels accurately.
- Ensure **data privacy**: do not store recordings, only track notification events.
- Optional: Send notifications as rich embeds with server branding/logo.

---

## Pseudocode Example

```python
active_recordings = set()

@bot.event
async def on_voice_state_update(member, before, after):
  if member.bot and "craig" in member.name.lower():
      if after.channel and member not in active_recordings:
          active_recordings.add(after.channel.id)
          await notify_channel_members(after.channel)
      if before.channel and not after.channel:
          active_recordings.discard(before.channel.id)
  elif after.channel and after.channel.id in active_recordings:
      await notify_user(member, after.channel)
Expected Behavior
Craig joins a voice channel → all users DMed immediately.

New users join the channel during recording → receive DMs automatically.

Users can open a ticket to request removal within 24 hours.

Notifications are logged for audit purposes.

Craig leaves → active recording tracking ends.