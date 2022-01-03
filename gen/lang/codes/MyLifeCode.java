while(me.isAlive()){
    me.coding();
    if (me.getCode().haveProplem()) {
        Gogle.serch("How to do fix " + me.getCode().getProplem());
        me.fixCode();
    }
}