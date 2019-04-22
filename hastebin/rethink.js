var r = require('rethinkdbdash')({
    servers: [
        {host: 'rdb', port: 28015},
    ]
});

r.dbCreate('haste').run();
r.db('haste').tableCreate('uploads').run();