[
  {
    '$group': {
      '_id': null, 
      'horizontal': {
        '$push': '$row'
      }
    }
  }, {
    '$set': {
      '_w': {
        '$strLenCP': {
          '$first': '$horizontal'
        }
      }, 
      '_h': {
        '$size': '$horizontal'
      }
    }
  }, {
    '$set': {
      'matrix': {
        '$map': {
          'input': {
            '$range': [
              0, '$_h'
            ]
          }, 
          'as': 'i', 
          'in': {
            '$map': {
              'input': {
                '$range': [
                  0, '$_w'
                ]
              }, 
              'as': 'j', 
              'in': {
                '$substrCP': [
                  {
                    '$arrayElemAt': [
                      '$horizontal', '$$i'
                    ]
                  }, '$$j', 1
                ]
              }
            }
          }
        }
      }
    }
  }, {
    '$set': {
      'matches': {
        '$map': {
          'input': {
            '$range': [
              1, {
                '$subtract': [
                  '$_h', 1
                ]
              }
            ]
          }, 
          'as': 'i', 
          'in': {
            '$map': {
              'input': {
                '$range': [
                  1, {
                    '$subtract': [
                      '$_w', 1
                    ]
                  }
                ]
              }, 
              'as': 'j', 
              'in': {
                '$let': {
                  'vars': {
                    'a': {
                      '$arrayElemAt': [
                        {
                          '$arrayElemAt': [
                            '$matrix', '$$i'
                          ]
                        }, '$$j'
                      ]
                    }, 
                    'tl': {
                      '$arrayElemAt': [
                        {
                          '$arrayElemAt': [
                            '$matrix', {
                              '$subtract': [
                                '$$i', 1
                              ]
                            }
                          ]
                        }, {
                          '$subtract': [
                            '$$j', 1
                          ]
                        }
                      ]
                    }, 
                    'tr': {
                      '$arrayElemAt': [
                        {
                          '$arrayElemAt': [
                            '$matrix', {
                              '$subtract': [
                                '$$i', 1
                              ]
                            }
                          ]
                        }, {
                          '$add': [
                            '$$j', 1
                          ]
                        }
                      ]
                    }, 
                    'bl': {
                      '$arrayElemAt': [
                        {
                          '$arrayElemAt': [
                            '$matrix', {
                              '$add': [
                                '$$i', 1
                              ]
                            }
                          ]
                        }, {
                          '$subtract': [
                            '$$j', 1
                          ]
                        }
                      ]
                    }, 
                    'br': {
                      '$arrayElemAt': [
                        {
                          '$arrayElemAt': [
                            '$matrix', {
                              '$add': [
                                '$$i', 1
                              ]
                            }
                          ]
                        }, {
                          '$add': [
                            '$$j', 1
                          ]
                        }
                      ]
                    }
                  }, 
                  'in': {
                    '$and': [
                      {
                        '$eq': [
                          '$$a', 'A'
                        ]
                      }, {
                        '$cond': {
                          'if': {
                            '$or': [
                              {
                                '$and': [
                                  {
                                    '$eq': [
                                      '$$tl', 'M'
                                    ]
                                  }, {
                                    '$eq': [
                                      '$$br', 'S'
                                    ]
                                  }
                                ]
                              }, {
                                '$and': [
                                  {
                                    '$eq': [
                                      '$$tl', 'S'
                                    ]
                                  }, {
                                    '$eq': [
                                      '$$br', 'M'
                                    ]
                                  }
                                ]
                              }
                            ]
                          }, 
                          'then': {
                            '$or': [
                              {
                                '$and': [
                                  {
                                    '$eq': [
                                      '$$tr', 'M'
                                    ]
                                  }, {
                                    '$eq': [
                                      '$$bl', 'S'
                                    ]
                                  }
                                ]
                              }, {
                                '$and': [
                                  {
                                    '$eq': [
                                      '$$tr', 'S'
                                    ]
                                  }, {
                                    '$eq': [
                                      '$$bl', 'M'
                                    ]
                                  }
                                ]
                              }
                            ]
                          }, 
                          'else': false
                        }
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
  }, {
    '$project': {
      '_id': 0, 
      'res': {
        '$size': {
          '$reduce': {
            'input': '$matches', 
            'initialValue': [], 
            'in': {
              '$concatArrays': [
                '$$value', {
                  '$filter': {
                    'input': '$$this', 
                    'as': 'b', 
                    'cond': '$$b'
                  }
                }
              ]
            }
          }
        }
      }
    }
  }
]
