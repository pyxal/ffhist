#!/bin/sh

# copy mozilla hist db
cp ~/".mozilla/firefox/$USER.default/places.sqlite" ~/.places.sqlite

# extract from db
sqlite3 ~/.places.sqlite <<EOF

-- temporary output file
.output .tempHist

-- query db
select last_visit_date, url from moz_places order by last_visit_date desc
EOF

# print list
python3 ~/.printList.py


# clean up temp files
rm ~/.places.sqlite
rm ~/.tempHist
