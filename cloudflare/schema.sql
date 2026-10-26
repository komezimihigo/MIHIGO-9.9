CREATE TABLE IF NOT EXISTS jobs (
 job_id TEXT PRIMARY KEY, source_url TEXT NOT NULL, source_kind TEXT NOT NULL,
 state TEXT NOT NULL DEFAULT 'DISCOVERED', output_format TEXT NOT NULL DEFAULT 'short',
 channel_id TEXT NOT NULL DEFAULT '', source_license TEXT NOT NULL DEFAULT '',
 license_url TEXT NOT NULL DEFAULT '', creator TEXT NOT NULL DEFAULT '',
 attribution TEXT NOT NULL DEFAULT '', rights_evidence TEXT NOT NULL DEFAULT '',
 output_key TEXT NOT NULL DEFAULT '', youtube_video_id TEXT NOT NULL DEFAULT '',
 attempts INTEGER NOT NULL DEFAULT 0, last_error TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_jobs_state ON jobs(state,created_at);
CREATE TABLE IF NOT EXISTS events(event_id INTEGER PRIMARY KEY AUTOINCREMENT,job_id TEXT,level TEXT,event TEXT,message TEXT,created_at TEXT);
CREATE TABLE IF NOT EXISTS channels(channel_id TEXT PRIMARY KEY,display_name TEXT NOT NULL,enabled INTEGER NOT NULL DEFAULT 0,privacy_status TEXT NOT NULL DEFAULT 'private',daily_target INTEGER NOT NULL DEFAULT 20);
CREATE TABLE IF NOT EXISTS publish_history(job_id TEXT PRIMARY KEY,channel_id TEXT NOT NULL,youtube_video_id TEXT NOT NULL,output_format TEXT NOT NULL,published_at TEXT NOT NULL);
