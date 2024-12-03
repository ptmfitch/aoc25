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
        'dos': {
          '$regexFindAll': {
            'input': '$memory', 
            'regex': new RegExp('do\(\)')
          }
        }, 
        'donts': {
          '$regexFindAll': {
            'input': '$memory', 
            'regex': new RegExp('don\'t\(\)')
          }
        }, 
        'matches': {
          '$regexFindAll': {
            'input': '$memory', 
            'regex': new RegExp('mul\((\d{1,3},\d{1,3})\)')
          }
        }
      }
    }, {
      '$set': {
        'dos': {
          '$concatArrays': [
            [
              0
            ], '$dos.idx'
          ]
        }, 
        'donts': {
          '$concatArrays': [
            '$donts.idx', [
              {
                '$strLenCP': '$memory'
              }
            ]
          ]
        }
      }
    }, {
      '$set': {
        'ranges': {
          '$map': {
            'input': '$dos', 
            'as': 'do', 
            'in': [
              '$$do', {
                '$first': {
                  '$filter': {
                    'input': '$donts', 
                    'as': 'dont', 
                    'cond': {
                      '$gt': [
                        '$$dont', '$$do'
                      ]
                    }
                  }
                }
              }
            ]
          }
        }
      }
    }, {
      '$set': {
        'ranges': {
          '$map': {
            'input': '$ranges', 
            'as': 'range', 
            'in': {
              '$range': [
                {
                  '$arrayElemAt': [
                    '$$range', 0
                  ]
                }, {
                  '$arrayElemAt': [
                    '$$range', 1
                  ]
                }
              ]
            }
          }
        }
      }
    }, {
      '$set': {
        'valid_idxs': {
          '$reduce': {
            'input': '$ranges', 
            'initialValue': [], 
            'in': {
              '$concatArrays': [
                '$$value', '$$this'
              ]
            }
          }
        }
      }
    }, {
      '$set': {
        'matches': {
          '$filter': {
            'input': '$matches', 
            'as': 'match', 
            'cond': {
              '$in': [
                '$$match.idx', '$valid_idxs'
              ]
            }
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