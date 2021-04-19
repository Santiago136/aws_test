from app.settings import DATABASE


def migrate():
    dynamodb = DATABASE

    table = dynamodb.create_table(
        TableName='Food',
        KeySchema=[
            {
                'AttributeName': 'product',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'product',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName='food')

    print(table.item_count)

    table.put_item(Item={
        'product': 'banana',
        'color': 'yellow',
        'is_tasty': True
    })

    table.put_item(Item={
        'product': 'tomato',
        'color': 'red'
    })

    table.put_item(Item={
        'product': 'orange',
        'color': 'orange',
        'additional': {
            'allergic': True
        }
    })
