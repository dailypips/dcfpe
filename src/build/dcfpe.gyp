{
  'includes':[
    'common.gypi',
    'win_precompile.gypi'
  ],
  'targets':[
    {
      'target_name': 'all',
      'type': 'none',
      'sources':[],
      'dependencies':[
        '<(DEPTH)\\dpe_base\\dpe_base.gyp:dpe_base',
        '<(DEPTH)\\process\\process.gyp:process',
        '<(DEPTH)\\dpe_service\\dpe_service.gyp:dpe_service',
        '<(DEPTH)\\dpe_service\\dpe_service.gyp:base_test',
        '<(DEPTH)\\dpe_service\\dpe_service.gyp:publisher',
        '<(DEPTH)\\dpe_service\\dpe_service.gyp:subscriber',
        ],
    }
    ]
}