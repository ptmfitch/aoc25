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
        'ls': {
          '$sortArray': {
            'input': '$ls', 
            'sortBy': 1
          }
        }, 
        'rs': {
          '$sortArray': {
            'input': '$rs', 
            'sortBy': 1
          }
        }
      }
    }, {
      '$set': {
        'res': {
          '$sum': {
            '$map': {
              'input': {
                '$range': [
                  0, {
                    '$size': '$ls'
                  }
                ]
              }, 
              'as': 'i', 
              'in': {
                '$abs': {
                  '$subtract': [
                    {
                      '$arrayElemAt': [
                        '$ls', '$$i'
                      ]
                    }, {
                      '$arrayElemAt': [
                        '$rs', '$$i'
                      ]
                    }
                  ]
                }
              }
            }
          }
        }
      }
    }
  ]