[
    {
      '$project': {
        '_id': 0, 
        'report': {
          '$map': {
            'input': {
              '$split': [
                '$reports', ' '
              ]
            }, 
            'in': {
              '$toInt': '$$this'
            }
          }
        }
      }
    }, {
      '$set': {
        'direction': {
          '$cond': {
            'if': {
              '$lt': [
                {
                  '$first': '$report'
                }, {
                  '$last': '$report'
                }
              ]
            }, 
            'then': 'increasing', 
            'else': 'decreasing'
          }
        }
      }
    }, {
      '$project': {
        'safe': {
          '$reduce': {
            'input': {
              '$range': [
                0, {
                  '$subtract': [
                    {
                      '$size': '$report'
                    }, 1
                  ]
                }
              ]
            }, 
            'initialValue': true, 
            'in': {
              '$let': {
                'vars': {
                  'distance': {
                    '$subtract': [
                      {
                        '$arrayElemAt': [
                          '$report', '$$this'
                        ]
                      }, {
                        '$arrayElemAt': [
                          '$report', {
                            '$add': [
                              '$$this', 1
                            ]
                          }
                        ]
                      }
                    ]
                  }
                }, 
                'in': {
                  '$cond': {
                    'if': {
                      '$not': '$$value'
                    }, 
                    'then': '$$value', 
                    'else': {
                      '$cond': {
                        'if': {
                          '$eq': [
                            '$direction', 'decreasing'
                          ]
                        }, 
                        'then': {
                          '$and': [
                            {
                              '$gt': [
                                '$$distance', 0
                              ]
                            }, {
                              '$lt': [
                                '$$distance', 4
                              ]
                            }
                          ]
                        }, 
                        'else': {
                          '$and': [
                            {
                              '$lt': [
                                '$$distance', 0
                              ]
                            }, {
                              '$gt': [
                                '$$distance', -4
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
          }
        }
      }
    }, {
      '$match': {
        'safe': true
      }
    }, {
      '$count': 'res'
    }
  ]