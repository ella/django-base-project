# cron jobs for centrum-djangobaselibrary-djangobaseproject package
*/5 * * * * root run-parts /centrum/djangobaselibrary/djangobaseproject/cron/every5min &>/dev/null
10 2 * * * root run-parts /centrum/djangobaselibrary/djangobaseproject/cron/daily &>/dev/null

