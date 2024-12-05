[
    {
      '$project': {
        '_id': 0, 
        'l': {
          '$toInt': {
            '$substrCP': [
              '$row', 0, 5
            ]
          }
        }, 
        'r': {
          '$toInt': {
            '$substrCP': [
              '$row', 8, 13
            ]
          }
        }
      }
    }, {
      '$group': {
        '_id': null, 
        'ls': {
          '$push': '$l'
        }, 
        'rs': {
          '$push': '$r'
        }
      }
    }, {
      '$set': {
        'mults': {
          '$map': {
            'input': '$ls', 
            'as': 'l', 
            'in': {
              '$multiply': [
                '$$l', {
                  '$size': {
                    '$filter': {
                      'input': '$rs', 
                      'as': 'r', 
                      'cond': {
                        '$eq': [
                          '$$l', '$$r'
                        ]
                      }
                    }
                  }
                }
              ]
            }
          }
        }
      }
    }, {
      '$set': {
        'res': {
          '$sum': '$mults'
        }
      }
    }
  ]