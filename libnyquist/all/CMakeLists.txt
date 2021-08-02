cmake_minimum_required(VERSION 3.5)

project(libnyquist)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library( libnyquist STATIC )

list( APPEND SOURCES
   PRIVATE
      # libnyquist

      ${CMAKE_SOURCE_DIR}/src/nyx.c

      # libnyquist/nyquist/cmt

      ${CMAKE_SOURCE_DIR}/nyquist/cmt/cext.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/cleanup.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/cmdline.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/cmtcmd.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/mem.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/midifile.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/midifns.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/moxc.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/record.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/seq.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/seqmread.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/seqmwrite.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/seqread.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/seqwrite.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/tempomap.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/timebase.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmt/userio.c

      # libnyquist/nyquist/cmupv

      ${CMAKE_SOURCE_DIR}/nyquist/cmupv/src/cmupv.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmupv/src/cmupvdbg.c
      ${CMAKE_SOURCE_DIR}/nyquist/cmupv/src/internal.c

      # libnyquist/nyquist/ffts

      ${CMAKE_SOURCE_DIR}/nyquist/ffts/src/fftext.c
      ${CMAKE_SOURCE_DIR}/nyquist/ffts/src/fftlib.c
      ${CMAKE_SOURCE_DIR}/nyquist/ffts/src/matlib.c

      # libnyquist/nyquist/nyqsrc

      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/add.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/avg.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/compose.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/convolve.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/debug.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/downsample.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/f0.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/falloc.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/ffilterkit.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/fft.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/handlers.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/inverse.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/local.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/lpanal.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/multiread.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/multiseq.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/phasevocoder.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/probe.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/pvshell.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/resamp.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/resampv.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/samples.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/seqext.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/seqfnint.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/seqinterf.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sliderdata.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sndfnint.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sndmax.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sndread.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sndseq.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sndsliders.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sndwritepa.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/sound.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/stats.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/stoponzero.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/trigger.c
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc/yin.c

      # libnyquist/nyquist/nyqstk

      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/instr.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/stkinit.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/stkint.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/ADSR.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/BandedWG.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/BiQuad.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Bowed.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/BowTable.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Chorus.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Clarinet.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Delay.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/DelayA.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/DelayL.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Effect.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Envelope.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/FileRead.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/FileWvIn.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Filter.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Flute.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Function.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Generator.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Instrmnt.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/JCRev.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/JetTable.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Mandolin.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Modal.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/ModalBar.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Noise.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/NRev.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/OnePole.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/OneZero.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/PitShift.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/PluckTwo.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/PoleZero.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/PRCRev.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/ReedTable.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Saxofony.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/SineWave.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Sitar.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/Stk.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/WaveLoop.cpp
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/src/WvIn.cpp


      # libnyquist/nyquist/sys

      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/macaboutbox.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/MacAE.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/MacCommandWin.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/macdrag.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/MacFileUtils.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/macfun.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/MacHandleEv.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/macint.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/macstuff.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/mac/xlextstart.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/unix/io.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/unix/osstuff.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/unix/term.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/unix/termtest.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/win/msvc/winfun.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/win/msvc/winstuff.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/win/wingui/winguistuff.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/win/wingui/xlextstart.c
      #${CMAKE_SOURCE_DIR}/nyquist/sys/win/wingui/xlispfns.c

      # libnyquist/nyquist/tran

      ${CMAKE_SOURCE_DIR}/nyquist/tran/abs.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/allpoles.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/alpass.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/alpasscv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/alpassvc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/alpassvv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/amosc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/areson.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/aresoncv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/aresonvc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/aresonvv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/atone.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/atonev.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/biquadfilt.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/buzz.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/chase.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/clip.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/congen.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/const.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/coterm.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/delaycc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/delaycv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/eqbandvvv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/exp.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/fmfb.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/fmfbv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/fmosc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/follow.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/fromarraystream.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/fromobject.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/gate.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/ifft.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrbanded.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrbow.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrbowedfreq.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrclar.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrclarall.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrclarfreq.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrflute.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrfluteall.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrflutefreq.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrmandolin.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrmodalbar.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrsax.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrsaxall.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrsaxfreq.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/instrsitar.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/integrate.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/log.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/lpreson.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/maxv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/offset.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/oneshot.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/osc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/partial.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/pluck.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/prod.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/pwl.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/quantize.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/recip.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/reson.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/resoncv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/resonvc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/resonvv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/sampler.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/scale.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/shape.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/sine.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/siosc.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/slope.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/sqrt.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/stkchorus.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/stkpitshift.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/stkrev.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/tapf.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/tapv.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/tone.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/tonev.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/upsample.c
      ${CMAKE_SOURCE_DIR}/nyquist/tran/white.c

      # libnyquist/nyquist/xlisp

      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/extern.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/path.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/security.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlbfun.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlcont.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xldbug.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xldmem.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xleval.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlfio.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlftab.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlglob.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlimage.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlinit.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlio.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlisp.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xljump.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xllist.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlmath.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlobj.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlpp.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlprin.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlread.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlstr.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlsubr.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlsym.c
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp/xlsys.c
)

list( APPEND INCLUDES
   PRIVATE
      ${CMAKE_SOURCE_DIR}/nyquist/cmt
      ${CMAKE_SOURCE_DIR}/nyquist/cmupv/src
      ${CMAKE_SOURCE_DIR}/nyquist/ffts/src
      ${CMAKE_SOURCE_DIR}/nyquist/nyqsrc
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk
      ${CMAKE_SOURCE_DIR}/nyquist/nyqstk/include
      ${CMAKE_SOURCE_DIR}/nyquist/tran
      ${CMAKE_SOURCE_DIR}/nyquist/xlisp
      $<$<BOOL:${UNIX}>:${CMAKE_SOURCE_DIR}/nyquist/sys/unix>
      $<$<NOT:$<BOOL:${UNIX}>>:${CMAKE_SOURCE_DIR}/nyquist/sys/win/msvc>
   PUBLIC
      ${CMAKE_SOURCE_DIR}/src
)

list( APPEND DEFINES
   PRIVATE
      CMTSTUFF
      EXT
      $<$<PLATFORM_ID:Windows>:WIN32>
)

list( APPEND OPTIONS
   PRIVATE
      $<$<PLATFORM_ID:Darwin>:-fno-common>
)


target_sources( libnyquist PUBLIC ${SOURCES} )
target_compile_definitions( libnyquist PUBLIC ${DEFINES} )
target_compile_options( libnyquist PUBLIC ${OPTIONS} )
target_include_directories( libnyquist PUBLIC ${INCLUDES} )
target_link_libraries( libnyquist PUBLIC CONAN_PKG::libsndfile CONAN_PKG::portaudio )

install(TARGETS libnyquist)

install(DIRECTORY "${CMAKE_SOURCE_DIR}/src/" DESTINATION include/ FILES_MATCHING PATTERN "*.h")
install(DIRECTORY "${CMAKE_SOURCE_DIR}/nyquist/cmt" DESTINATION include/cmt FILES_MATCHING PATTERN "*.h")
install(DIRECTORY "${CMAKE_SOURCE_DIR}/nyquist/nyqstk/include" DESTINATION include/xlisp FILES_MATCHING PATTERN "*.h")
install(DIRECTORY "${CMAKE_SOURCE_DIR}/nyquist/tran" DESTINATION include/tran FILES_MATCHING PATTERN "*.h")
install(DIRECTORY "${CMAKE_SOURCE_DIR}/nyquist/xlisp" DESTINATION include/xlisp FILES_MATCHING PATTERN "*.h")