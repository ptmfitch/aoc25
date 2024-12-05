[
    {
      '$group': {
        '_id': null, 
        'memory': {
          '$push': '$memory'
        }
      }
    }, {
      '$project': {
        '_id': 0, 
        'memory': {
          '$reduce': {
            'input': '$memory', 
            'initialValue': '', 
            'in': {
              '$concat': [
                '$$value', '$$this'
              ]
            }
          }
        }
      }
    }, {
      '$set': {
        'matches': {
          '$regexFindAll': {
            'input': '$memory', 
            'regex': new RegExp('mul\((\d{1,3},\d{1,3})\)')
          }
        }
      }
    }, {
      '$set': {
        'numbers': {
          '$map': {
            'input': '$matches.captures', 
            'as': 'captures', 
            'in': {
              '$map': {
                'input': {
                  '$split': [
                    {
                      '$arrayElemAt': [
                        '$$captures', 0
                      ]
                    }, ','
                  ]
                }, 
                'as': 'number', 
                'in': {
                  '$toInt': '$$number'
                }
              }
            }
          }
        }
      }
    }, {
      '$set': {
        'products': {
          '$map': {
            'input': '$numbers', 
            'as': 'pair', 
            'in': {
              '$multiply': [
                {
                  '$arrayElemAt': [
                    '$$pair', 0
                  ]
                }, {
                  '$arrayElemAt': [
                    '$$pair', 1
                  ]
                }
              ]
            }
          }
        }
      }
    }, {
      '$unwind': {
        'path': '$products'
      }
    }, {
      '$group': {
        '_id': null, 
        'res': {
          '$sum': '$products'
        }
      }
    }
  ]