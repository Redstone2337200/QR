```hs
# function ml:gnr/method/get/uuid
execute at @a[limit=1] run summon item_display ~ ~ ~ {item: {id:"minecraft:dirt",Count: 1b},view_range: 0.0f,UUID: [I;39003092,49405,949,20499]}
item modify entity 025323d4-0000-c0fd-0000-03b500005013 container.0 ml:gnr/method/uuid
data modify storage ca: tmp set value {}
data modify storage ca: tmp.string set from entity 025323d4-0000-c0fd-0000-03b500005013 item.tag.display.Name
function ml:gnr/method/get/z/uuid with storage ca: tmp
kill 025323d4-0000-c0fd-0000-03b500005013

# function ml:gnr/method/get/z/uuid
$data modify storage ca: tmp.string set value $(string)
data modify storage ca: output set value {}
data modify storage ca: output.uuid set from storage ca: tmp.string.hoverEvent.contents.id
```

& the item modifier:```json
// # item_modifier ml:gnr/method/uuid
{
    "function":"set_name",
    "entity": "this",
    "name": {
        "clickEvent": {
            "action": "suggest_command",
            "value":""
        },
        "insertion": "",
        "selector": "@s"
    }
}
```