#include "memory.h"
#include <iostream>
#include <fstream>
using namespace std;
#include "portSMF/allegro.h"

Alg_seq_ptr make_simple_score()
{
    Alg_seq_ptr seq = new Alg_seq;
    Alg_update_ptr update = seq->create_update(0, 0, -1);
    update->set_real_value("attackr", 0.007);
    seq->add_event(update, 0);

    Alg_note_ptr note = seq->create_note(0, 0, 63, 63, 105, 0.8);
    // at 100bpm, dur will be 1.33 beats
    seq->add_event(note, 0);

    // at 100bpm, time = W0.33 beats, dur = 0.66 beats

    note = seq->create_note(0.8, 0, 65, 65, 107, 0.4);
    seq->add_event(note, 0);
    //seq_print(seq);
    return seq;
}

int main()
{
    Alg_seq_ptr seq = make_simple_score();
    seq->write(cout, false);

    return 0;
}
