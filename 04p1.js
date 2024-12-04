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
      '_n': {
        '$strLenCP': 'XMAS'
      }, 
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
      'vertical': {
        '$map': {
          'input': {
            '$range': [
              0, '$_h'
            ]
          }, 
          'as': 'i', 
          'in': {
            '$reduce': {
              'input': {
                '$range': [
                  0, '$_w'
                ]
              }, 
              'initialValue': '', 
              'in': {
                '$concat': [
                  '$$value', {
                    '$substrCP': [
                      {
                        '$arrayElemAt': [
                          '$horizontal', '$$this'
                        ]
                      }, '$$i', 1
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }, {
    '$set': {
      'diagonal_r': {
        '$concatArrays': [
          {
            '$map': {
              'input': {
                '$range': [
                  0, {
                    '$subtract': [
                      '$_w', {
                        '$subtract': [
                          '$_n', 1
                        ]
                      }
                    ]
                  }
                ]
              }, 
              'as': 'i', 
              'in': {
                '$reduce': {
                  'input': {
                    '$range': [
                      0, {
                        '$subtract': [
                          '$_w', '$$i'
                        ]
                      }
                    ]
                  }, 
                  'initialValue': '', 
                  'in': {
                    '$concat': [
                      '$$value', {
                        '$substrCP': [
                          {
                            '$arrayElemAt': [
                              '$horizontal', '$$this'
                            ]
                          }, {
                            '$add': [
                              '$$this', '$$i'
                            ]
                          }, 1
                        ]
                      }
                    ]
                  }
                }
              }
            }
          }, {
            '$map': {
              'input': {
                '$range': [
                  1, {
                    '$subtract': [
                      '$_h', {
                        '$subtract': [
                          '$_n', 1
                        ]
                      }
                    ]
                  }
                ]
              }, 
              'as': 'i', 
              'in': {
                '$reduce': {
                  'input': {
                    '$range': [
                      0, {
                        '$subtract': [
                          '$_h', '$$i'
                        ]
                      }
                    ]
                  }, 
                  'initialValue': '', 
                  'in': {
                    '$concat': [
                      '$$value', {
                        '$substrCP': [
                          {
                            '$arrayElemAt': [
                              '$horizontal', {
                                '$add': [
                                  '$$this', '$$i'
                                ]
                              }
                            ]
                          }, '$$this', 1
                        ]
                      }
                    ]
                  }
                }
              }
            }
          }
        ]
      }
    }
  }, {
    '$set': {
      'diagonal_l': {
        '$concatArrays': [
          {
            '$map': {
              'input': {
                '$range': [
                  {
                    '$subtract': [
                      '$_w', 1
                    ]
                  }, {
                    '$subtract': [
                      '$_n', 2
                    ]
                  }, -1
                ]
              }, 
              'as': 'i', 
              'in': {
                '$reduce': {
                  'input': {
                    '$range': [
                      0, {
                        '$add': [
                          '$$i', 1
                        ]
                      }
                    ]
                  }, 
                  'initialValue': '', 
                  'in': {
                    '$concat': [
                      '$$value', {
                        '$substrCP': [
                          {
                            '$arrayElemAt': [
                              '$horizontal', '$$this'
                            ]
                          }, {
                            '$subtract': [
                              '$$i', '$$this'
                            ]
                          }, 1
                        ]
                      }
                    ]
                  }
                }
              }
            }
          }, {
            '$map': {
              'input': {
                '$range': [
                  1, {
                    '$subtract': [
                      '$_h', {
                        '$subtract': [
                          '$_n', 1
                        ]
                      }
                    ]
                  }
                ]
              }, 
              'as': 'i', 
              'in': {
                '$reduce': {
                  'input': {
                    '$range': [
                      {
                        '$subtract': [
                          '$_w', 1
                        ]
                      }, {
                        '$subtract': [
                          '$$i', 1
                        ]
                      }, -1
                    ]
                  }, 
                  'initialValue': '', 
                  'in': {
                    '$concat': [
                      '$$value', {
                        '$substrCP': [
                          {
                            '$arrayElemAt': [
                              '$horizontal', {
                                '$add': [
                                  {
                                    '$subtract': [
                                      '$$i', 1
                                    ]
                                  }, {
                                    '$subtract': [
                                      '$_w', '$$this'
                                    ]
                                  }
                                ]
                              }
                            ]
                          }, '$$this', 1
                        ]
                      }
                    ]
                  }
                }
              }
            }
          }
        ]
      }
    }
  }, {
    '$set': {
      'flattened': {
        '$concatArrays': [
          '$horizontal', '$vertical', '$diagonal_r', '$diagonal_l'
        ]
      }
    }
  }, {
    '$set': {
      'f_matches': {
        '$map': {
          'input': '$flattened', 
          'as': 's', 
          'in': {
            '$regexFindAll': {
              'input': '$$s', 
              'regex': new RegExp('XMAS')
            }
          }
        }
      }, 
      'b_matches': {
        '$map': {
          'input': '$flattened', 
          'as': 's', 
          'in': {
            '$regexFindAll': {
              'input': '$$s', 
              'regex': new RegExp('SAMX')
            }
          }
        }
      }
    }
  }, {
    '$set': {
      'all_matches': {
        '$reduce': {
          'input': {
            '$concatArrays': [
              '$f_matches', '$b_matches'
            ]
          }, 
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
    '$project': {
      'res': {
        '$size': '$all_matches'
      }
    }
  }
]
