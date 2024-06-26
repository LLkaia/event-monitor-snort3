reputation =
{
    blocklist = BLACK_LIST_PATH .. '/default.blocklist'
}

ips =
{
    enable_builtin_rules = true,
    include = RULE_PATH .. "/pulledpork.rules",
    variables = default_variables
}

suppress =
{
    { gid = 116, sid = 6 },
    { gid = 112, sid = 1 }
}

alert_json = 
{
    file = true,
    limit = 0,
    fields = 'seconds action dst_addr dst_port msg proto sid rev gid src_addr src_port',
}

perf_monitor =
{
    modules = {},
    format = 'json',
    packets = 0
}

profiler =
{
    modules = {show = false},
    memory = {show = false},
    rules = {count = 10}
}
