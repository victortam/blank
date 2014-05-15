from dteam import datastores
ds = datastores.bi()

def fetch_trials(q_date):

    with datastores.CursorFrom(ds.bizdw_v6_pool, autocommit=True) as cur:

        cur.execute("""select count(*)
                         from bizdw_v6.lifecycle_events_trials t
                         where t.fk_daily_datetime_id = %i""" % int(q_date))

        return [ row for row in cur ][0][0]


# MAIN

if __name__ == '__main__':

    trials = fetch_trials(20140505) 
    print(trials)

