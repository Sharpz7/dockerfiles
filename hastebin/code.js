var r = require('rethinkdbdash')();

r.dbCreate('haste').run();
r.db('heroes').tableCreate('uploads').run();