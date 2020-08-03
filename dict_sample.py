from collections import Counter, defaultdict

items = [
    {'service': 'AAAA', 'id': 'A01', 'status': 'submitted', 'name': 'Tom', 'is_new': ''},
    {'service': 'AAAA', 'id': 'A02', 'status': 'canceled', 'name': 'Mike', 'is_new': True},
    {'service': 'AAAA', 'id': 'A03', 'status': 'submitted', 'name': 'Mary', 'is_new': ''},
    {'service': 'BBB', 'id': 'B01', 'status': 'submitted', 'name': 'Jon', 'is_new': ''},
    {'service': 'BBB', 'id': 'B02', 'status': 'submitted', 'name': 'Taro', 'is_new': ''},
    {'service': 'CC', 'id': 'C01', 'status': 'canceled', 'name': 'Miki', 'is_new': ''},
    {'service': 'CC', 'id': 'C02', 'status': 'submitted', 'name': 'Ken', 'is_new': ''},
    {'service': 'CC', 'id': 'C03', 'status': 'submitted', 'name': 'Kenny', 'is_new': True},
    {'service': 'CC', 'id': 'C04', 'status': 'submitted', 'name': 'Juddy', 'is_new': ''},
    {'service': 'CC', 'id': 'C05', 'status': 'submitted', 'name': 'Donna', 'is_new': ''},
]
# print(f"items={items}")
# サービスごとの件数カウント
inputs_counter = Counter([x.get('service') for x in items])
print(f"inputs_counter={inputs_counter}")
# サービスごとの'is_new'の件数カウント
inputs_counter_new = Counter([x.get('service') for x in items if x.get('is_new')])
print(f"inputs_counter_new={inputs_counter_new}")

# 数え上げ
items_counter = defaultdict(int)
for item in items:
    items_counter[item['service']] += 1
print(f"items_counter={items_counter}")

# サービスごとにlistをまとめ上げ
service_dict = defaultdict(list)
for key in inputs_counter.keys():
    for item in items:
        service_dict[key].append(item) if key in item.values() else None

# サービスごとに必要な情報をカウント
agg_dict = {}
for service, items_list in service_dict.items():
    agg_dict.update(
        {
            service: {
                'total_count': len(items_list),
                'is_new_count': len([x for x in items_list if x.get('is_new')]),
                'status_count': Counter([x.get('status') for x in items_list]),
            }
        }
    )

# 元リストを追加
agg_dict.update({'items': items})
print(f"agg_dict={agg_dict}")
print(f"status_count.submitted={agg_dict.get('AAAA').get('status_count').get('submitted')}")